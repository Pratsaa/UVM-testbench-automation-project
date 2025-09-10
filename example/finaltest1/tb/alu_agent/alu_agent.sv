`ifndef ALU_AGENT_SV
`define ALU_AGENT_SV

class alu_agent extends uvm_agent;
  `uvm_component_utils(alu_agent)

  alu_driver m_driver;
  alu_monitor m_monitor;
  uvm_sequencer #(alu_seq_item) m_seqr;
  virtual alu_if vif;
  uvm_active_passive_enum m_active = UVM_ACTIVE;

  function new(string name = "alu_agent", uvm_component parent = null);
    super.new(name,parent);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    if (m_active == UVM_ACTIVE) begin
      m_driver = alu_driver::type_id::create("m_driver", this);
      m_seqr = uvm_sequencer#(alu_seq_item)::type_id::create("m_seqr", this);
    end
    m_monitor = alu_monitor::type_id::create("m_monitor", this);
  endfunction

  virtual function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
    if (!uvm_config_db#(virtual alu_if)::get(this, "", "alu_if", vif)) begin
      `uvm_fatal(get_type_name(), "cannot access the interface")
    end
     else begin
      `uvm_info("AGT", "able to access the interface", UVM_LOW)
    end

    if (m_active == UVM_ACTIVE) begin
      m_driver.vif = vif;
      m_driver.seq_item_port.connect(m_seqr.seq_item_export);
       `uvm_info("AGT","connected m_drv.seq_item_port -> m_seqr.seq_item_export", UVM_LOW)
    end
    m_monitor.vif = vif;
  endfunction

endclass

`endif
