module tt_um_pqc_aishu (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,

    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,

    input  wire ena,
    input  wire clk,
    input  wire rst_n
);

    reg [7:0] lfsr;

    wire feedback;

    assign feedback = lfsr[7] ^ lfsr[5] ^ lfsr[4] ^ lfsr[3];

    always @(posedge clk or negedge rst_n)
    begin
        if (!rst_n)
            lfsr <= 8'hA5;

        else if (uio_in[0])
            lfsr <= ui_in;

        else
            lfsr <= {lfsr[6:0], feedback};
    end

    assign uo_out = lfsr;

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

endmodule
