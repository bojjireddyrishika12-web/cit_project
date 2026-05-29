# How it works

This project implements an 8-bit pseudo-random number generator using a Linear Feedback Shift Register (LFSR). A seed value can be loaded through the input bus, and a new pseudo-random value is generated on every clock cycle.

# How to test

1. Apply reset.
2. Load an 8-bit seed using ui_in.
3. Set uio_in[0] high for one clock cycle.
4. Observe uo_out changing every clock cycle.
5. Verify that the generated sequence follows LFSR behavior.
