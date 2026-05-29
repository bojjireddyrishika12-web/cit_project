# 8-bit Random Number Generator

## Description

This project implements an 8-bit pseudo-random number generator using a Linear Feedback Shift Register (LFSR).

The generator produces a random-looking sequence of numbers on every clock cycle.

## Inputs

| Signal | Function |
|----------|----------|
| ui_in[7:0] | Seed Value |
| uio_in[0] | Load Seed |
| clk | System Clock |
| rst_n | Active-Low Reset |

## Outputs

| Signal | Function |
|----------|----------|
| uo_out[7:0] | Random Number |

## Applications

- Cryptography
- Hardware Testing
- Gaming
- Digital Communication
- Data Scrambling
