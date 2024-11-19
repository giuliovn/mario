version 1.0 

workflow Hello {
  input {
    String name = "you"
  }

  call WriteGreeting {
    input:
      name = name
  }

  output{
    File out = WriteGreeting.output_greeting
  }
}

task WriteGreeting {
  input {
    String name = "you"
  }

  command {
     echo "Hello ~{name}!"
  }
  output {
     # Write output to standard out
     File output_greeting = stdout()
  }
}
