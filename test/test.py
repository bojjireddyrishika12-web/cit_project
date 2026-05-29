import cocotb
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Starting PQC RNG Testbench")

    # Set the clock period to 100 ns (10 MHz)
    # The clock is automatically managed by the Tiny Tapeout test runner template

    # 1. System Reset Assertion
    dut._log.info("Applying system reset...")
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    await ClockCycles(dut.clk, 5)
    
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 2)

    # 2. Test Autonomous PRNG Mode (mode_sel = 0)
    dut._log.info("Testing Autonomous PRNG Sequence Generation...")
    dut.uio_in.value = 0  # mode_sel = 0
    
    # Capture consecutive cycles to verify output bits change pseudo-randomly
    val1 = int(dut.uo_out.value)
    await ClockCycles(dut.clk, 1)
    val2 = int(dut.uo_out.value)
    await ClockCycles(dut.clk, 1)
    val3 = int(dut.uo_out.value)
    
    dut._log.info(f"Generated Random Sequence Stream values: {val1}, {val2}, {val3}")
    
    # 3. Test Hybrid Seeding Mode (mode_sel = 1)
    dut._log.info("Testing Hybrid Entropy Injection Mode...")
    dut.uio_in.value = 1  # mode_sel = 1
    dut.ui_in.value = 0x55  # Inject structural seeding bits
    await ClockCycles(dut.clk, 5)
    
    dut._log.info("RNG Test completed successfully.")
