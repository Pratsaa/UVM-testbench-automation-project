`ifndef ALU_MONITOR_SV
`define ALU_MONITOR_SV

class alu_monitor extends uvm_monitor;
  `uvm_component_utils(alu_monitor)

  virtual alu_if vif;
  uvm_analysis_port #(alu_seq_item) ap;

  function new(string name = "alu_monitor", uvm_component parent = null);
    super.new(name, parent);
    ap = new("ap", this);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    // if (!uvm_config_db#(virtual alu_if)::get(this, "", "alu_if", vif)) begin
    //   `uvm_fatal(get_type_name(), "Unable to get virtual interface")
    // end
  endfunction

  virtual task run_phase(uvm_phase phase);
    alu_seq_item tx;
    // forever begin
      // @(posedge vif.clk);
      // TODO: Add sampling logic here
      // tx = alu_seq_item::type_id::create("tx");
      // tx.field = vif.signal;
      // ap.write(tx);
    // end
  endtask

endclass

`endif
