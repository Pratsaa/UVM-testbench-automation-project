`ifndef ALU_DRIVER_SV
`define ALU_DRIVER_SV

class alu_driver extends uvm_driver#(alu_seq_item);
  `uvm_component_utils(alu_driver)

  virtual alu_if vif; 
  alu_seq_item req;

  function new(string name = "alu_agent", uvm_component parent = null);
    super.new(name,parent);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    req = alu_seq_item::type_id::create("req");
  endfunction

//   virtual function void connect_phase(uvm_phase phase);
//     super.connect_phase(phase);
//     if (!uvm_config_db#(virtual alu_if)::get(this, "", "alu_if", vif)) begin
//       `uvm_fatal(get_type_name(), "cannot access the interface")
//     end

  virtual task reset_phase(uvm_phase phase);
    super.reset_phase(phase);
    //Add all variables to be resetted here
  endtask

  virtual task run_phase(uvm_phase phase);
     super.run_phase(phase);
      forever begin
        seq_item_port.get_next_item(req);
        // TODO: Add code to drive the interface using req
        // Example: vif.some_signal <= req.some_value;
        seq_item_port.item_done();
      end
  endtask


endclass

`endif
