"""
Transformer encoder, built from scratch in PyTorch.

Run in VS Code:
    pip install torch --break-system-packages   (or in a venv: pip install torch)
    python transformer_from_scratch.py

Every step below matches the pipeline: text -> tokens -> IDs -> embeddings
-> positional encoding -> self-attention -> add&norm -> feed-forward ->
add&norm -> output. Each block prints its output shape so you can watch
the tensor move through the model.
"""

import math
import torch
import torch.nn as nn
import torch.nn.functional as F


# ---------------------------------------------------------------------------
# STEP 2-3: Tokenizer + token IDs
# A real model uses BPE/WordPiece over a huge vocab. Here's a minimal
# word-level version so the mechanics are visible.
# ---------------------------------------------------------------------------
class SimpleTokenizer:
    def __init__(self, text_corpus):
        vocab = sorted(set(text_corpus.lower().split()))
        self.stoi = {w: i + 1 for i, w in enumerate(vocab)}  # 0 = pad
        self.stoi["<pad>"] = 0
        self.itos = {i: w for w, i in self.stoi.items()}
        self.vocab_size = len(self.stoi)

    def encode(self, sentence):
        return [self.stoi[w] for w in sentence.lower().split()]


# ---------------------------------------------------------------------------
# STEP 5: Positional encoding
# Sinusoidal, fixed (not learned) — the original "Attention Is All You Need" scheme.
# ---------------------------------------------------------------------------
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=512):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1).float()
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer("pe", pe.unsqueeze(0))  # (1, max_len, d_model)

    def forward(self, x):
        # x: (batch, seq_len, d_model)
        return x + self.pe[:, : x.size(1)]


# ---------------------------------------------------------------------------
# STEP 6: Multi-head self-attention
# Every token builds a Query, Key, Value from its own vector.
# attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V
# ---------------------------------------------------------------------------
class MultiHeadSelfAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        assert d_model % n_heads == 0
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads

        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_out = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        batch, seq_len, _ = x.shape

        # Project input into Q, K, V, then split into heads.
        q = self.w_q(x).view(batch, seq_len, self.n_heads, self.d_k).transpose(1, 2)
        k = self.w_k(x).view(batch, seq_len, self.n_heads, self.d_k).transpose(1, 2)
        v = self.w_v(x).view(batch, seq_len, self.n_heads, self.d_k).transpose(1, 2)
        # q, k, v: (batch, n_heads, seq_len, d_k)

        # Scaled dot-product attention scores: how much each token attends to every other.
        scores = (q @ k.transpose(-2, -1)) / math.sqrt(self.d_k)  # (batch, n_heads, seq_len, seq_len)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float("-inf"))
        attn_weights = F.softmax(scores, dim=-1)

        # Weighted sum of Values.
        out = attn_weights @ v  # (batch, n_heads, seq_len, d_k)

        # Merge heads back into one vector per token.
        out = out.transpose(1, 2).contiguous().view(batch, seq_len, self.d_model)
        return self.w_out(out), attn_weights


# ---------------------------------------------------------------------------
# STEP 8: Position-wise feed-forward network
# Same small MLP applied independently to every token's vector.
# ---------------------------------------------------------------------------
class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Linear(d_ff, d_model),
        )

    def forward(self, x):
        return self.net(x)


# ---------------------------------------------------------------------------
# One full encoder layer: steps 6-9.
# ---------------------------------------------------------------------------
class EncoderLayer(nn.Module):
    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
        super().__init__()
        self.attn = MultiHeadSelfAttention(d_model, n_heads)
        self.norm1 = nn.LayerNorm(d_model)
        self.ff = FeedForward(d_model, d_ff)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        # Step 6: self-attention, then step 7: residual + norm.
        attn_out, attn_weights = self.attn(x, mask)
        x = self.norm1(x + self.dropout(attn_out))

        # Step 8: feed-forward, then step 9: residual + norm.
        ff_out = self.ff(x)
        x = self.norm2(x + self.dropout(ff_out))
        return x, attn_weights


# ---------------------------------------------------------------------------
# Full encoder: steps 4-10, stacking N encoder layers.
# ---------------------------------------------------------------------------
class TransformerEncoder(nn.Module):
    def __init__(self, vocab_size, d_model=64, n_heads=4, d_ff=256, n_layers=3, max_len=512):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)      # step 4
        self.pos_encoding = PositionalEncoding(d_model, max_len)  # step 5
        self.layers = nn.ModuleList(
            [EncoderLayer(d_model, n_heads, d_ff) for _ in range(n_layers)]
        )
        self.d_model = d_model

    def forward(self, token_ids, mask=None, verbose=False, trace=None):
        # trace is an optional dict that gets filled with real numbers at every
        # step, so a separate front-end (HTML/CSS/JS) can render this exact
        # forward pass instead of made-up example numbers.
        raw_embed = self.embedding(token_ids)
        x = raw_embed * math.sqrt(self.d_model)
        if verbose:
            print(f"[step 4] after embedding lookup:      {tuple(x.shape)}")
        if trace is not None:
            trace["embedding"] = raw_embed[0].detach().tolist()  # (seq_len, d_model), pre-scale

        # Step 5: add positional encoding.
        pos_only = self.pos_encoding.pe[0, : x.size(1)]
        x = self.pos_encoding(x)
        if verbose:
            print(f"[step 5] after + positional encoding: {tuple(x.shape)}")
        if trace is not None:
            trace["positional"] = pos_only.detach().tolist()      # (seq_len, d_model)
            trace["embed_plus_pos"] = x[0].detach().tolist()      # (seq_len, d_model)

        attn_weights_per_layer = []
        layer_traces = []
        for i, layer in enumerate(self.layers):
            pre = x
            x, attn_weights = layer(x, mask)
            attn_weights_per_layer.append(attn_weights)
            if verbose:
                print(f"[step 6-9] after encoder layer {i + 1}:    {tuple(x.shape)}")
            if trace is not None:
                # Average attention weights across heads -> one seq x seq matrix, easy to draw as a heatmap.
                avg_attn = attn_weights[0].mean(dim=0).detach().tolist()
                layer_traces.append({
                    "attention": avg_attn,
                    "pre_mean": pre[0].mean().item(),
                    "pre_std": pre[0].std().item(),
                    "post_mean": x[0].mean().item(),
                    "post_std": x[0].std().item(),
                    "output_sample": x[0].detach().tolist(),
                })

        if verbose:
            print(f"[step 10] final encoder output:       {tuple(x.shape)}")
        if trace is not None:
            trace["layers"] = layer_traces
            trace["final_output"] = x[0].detach().tolist()
        return x, attn_weights_per_layer


# ---------------------------------------------------------------------------
# Demo: walk one sentence through every step.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    corpus = "the cat sat on the mat the dog ran in the park"
    tokenizer = SimpleTokenizer(corpus)

    sentence = "the cat sat"
    ids = tokenizer.encode(sentence)
    print(f"[step 1] input text:      {sentence!r}")
    print(f"[step 2] tokens:          {sentence.split()}")
    print(f"[step 3] token IDs:       {ids}")

    token_ids = torch.tensor([ids])  # add batch dimension -> (1, seq_len)

    model = TransformerEncoder(
        vocab_size=tokenizer.vocab_size,
        d_model=64,
        n_heads=4,
        d_ff=256,
        n_layers=3,
    )

    trace = {"sentence": sentence, "tokens": sentence.split(), "token_ids": ids}
    output, attn_weights = model(token_ids, verbose=True, trace=trace)

    print("\nFinal output (contextualized vector per token):")
    print(output.shape, "-> one 64-dim vector for each of the 3 input tokens")
    print("\nAttention weights from layer 1, head 1 (rows=query token, cols=key token):")
    print(attn_weights[0][0, 0].detach())

    # ---------------------------------------------------------------------
    # Export the real numbers from this run to steps_data.js, so the
    # companion transformer_visualizer.html can render this exact forward
    # pass step by step in the browser.
    # ---------------------------------------------------------------------
    import json
    import os

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "steps_data.js")
    with open(out_path, "w") as f:
        f.write("const STEP_DATA = ")
        json.dump(trace, f)
        f.write(";\n")
    print(f"\nExported visualization data -> {out_path}")
    print("Open transformer_visualizer.html in a browser to step through it visually.")