`ifndef {name_upper}_MONITOR_SV
`define {name_upper}_MONITOR_SV

class {name}_monitor extends uvm_monitor;
  `uvm_component_utils({name}_monitor)

  virtual {name}_if vif;
  uvm_analysis_port #({name}_seq_item) ap;

  function new(string name = "{name}_monitor", uvm_component parent = null);
    super.new(name, parent);
    ap = new("ap", this);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    // if (!uvm_config_db#(virtual {name}_if)::get(this, "", "{name}_if", vif)) begin
    //   `uvm_fatal(get_type_name(), "Unable to get virtual interface")
    // end
  endfunction

  virtual task run_phase(uvm_phase phase);
    {name}_seq_item tx;
    // forever begin
      // @(posedge vif.clk);
      // TODO: Add sampling logic here
      // tx = {name}_seq_item::type_id::create("tx");
      // tx.field = vif.signal;
      // ap.write(tx);
    // end
  endtask

endclass

`endif
