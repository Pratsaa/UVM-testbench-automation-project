`ifndef UART_MONITOR_SV
`define UART_MONITOR_SV

class uart_monitor extends uvm_monitor;
  `uvm_component_utils(uart_monitor)

  virtual uart_if vif;
  uvm_analysis_port #(uart_seq_item) ap;

  function new(string name = "uart_monitor", uvm_component parent = null);
    super.new(name, parent);
    ap = new("ap", this);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    // if (!uvm_config_db#(virtual uart_if)::get(this, "", "uart_if", vif)) begin
    //   `uvm_fatal(get_type_name(), "Unable to get virtual interface")
    // end
  endfunction

  virtual task run_phase(uvm_phase phase);
    uart_seq_item tx;
    // forever begin
      // @(posedge vif.clk);
      // TODO: Add sampling logic here
      // tx = uart_seq_item::type_id::create("tx");
      // tx.field = vif.signal;
      // ap.write(tx);
    // end
  endtask

endclass

`endif
