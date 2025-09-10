`ifndef FINALTEST1_TEST_SV
`define FINALTEST1_TEST_SV

class finaltest1_test extends uvm_test;
  `uvm_component_utils(finaltest1_test)

  finaltest1_env m_env;
  finaltest1_basic_seq base_seq;

  function new(string name = "finaltest1_test", uvm_component parent = null);
    super.new(name, parent);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    string test_seq_name;
    uvm_factory factory = uvm_factory::get();
    super.build_phase(phase);

    if($value$plusargs("sim_test_seq_name=%0s", test_seq_name)) begin
      `uvm_info(get_type_name(), $sformatf("Overriding tb_base_sequence with %0s", test_seq_name), UVM_LOW)
      factory.set_type_override_by_name("tb_basic_seq", test_seq_name);
    end
    m_env = finaltest1_env::type_id::create("m_env", this);
  endfunction

  virtual task run_phase(uvm_phase phase);
    phase.raise_objection(this);

    // Run the main test sequence
    base_seq = finaltest1_basic_seq::type_id::create("base_seq");
    base_seq.start(m_env.m_alu_agent.m_seqr);

    #100;
    phase.drop_objection(this);
  endtask

endclass

`endif
