---
layout: post
title: Process creation in C vs Erlang
---

Process is the running instance of program, so to execute any program we need to create a process, there are various defined procedures depending on language for creation of process.

For example in **C**, we use `fork` and `spawn` in Erlang.
If you are a computer science student, you might have come across the term `fork` in your operating systems course, as far as **Erlang** is concerned you might not have heard about it.

Before I go to the process creation in both the languages, I will encourage you to read something about Erlang on internet.

## Process creation in C

```
  #include <stdio.h>
  #include <sys/types.h
  #include <unistd.h>
  #include <stdlib.h>
  #include <errno.h>
  int child = 0, parent = 0;
  int main(void){
  int numProcess = 10;
  for(int i=0; i<numProcess; i++){
    pid_t  pid;
    /* Output from both the child and the parent process
    * will be written to the standard output,
    * as they both run at the same time.
    */

    pid = fork();

    if (pid == -1){
      /* Error:
       * When fork() returns -1, an error happened
       * (for example, number of processes reached the limit).
       */
      fprintf(stderr, "can't fork, error %d\n", errno);
      exit(EXIT_FAILURE);
    }else if (pid == 0){
      /* Child process:
       */
       printf("\nchild process : %d\n",child);
       child+=1;
    }else{
      // parent process
      printf("\nparent process : %d\n",parent);
      parent+=1;
    }
  }
  return 0;
}
```
For executing this program save the code as *process_c.c* and then execute
  1. `gcc process_c.c`
  2. `./a.out`

You can the value of number of processes, change the value of numProcess in program

## Process creation in Erlang

```
-module(process_erlang).
-export([chain/1]).

chain(0) ->
	receive
		_ -> ok
	after 2000 ->
		process_flag(trap_exit, true)
	end;

chain(N) ->
	Pid = spawn(fun() -> chain(N-1) end),
	link(Pid),
	io:format("~nprocess ~p created, Pid :: ~p ~n",[N,Pid]),
	receive
		_ -> ok
	end.
```

For executing above Erlang code, save the file as *process_erlang.erl* then
  1. Start erl monitor by typing `erl` on terminal
  2. `c(process_erlang).`
  3. `link(spawn(process_erlang, chain, [100])).`

 At the place of `100` in step 3, you can set value of choice depending on number of processes.

## Comparison of process creation time

Processes of Erlang are very light weight as compared to processes of C and thus time taken by Erlang processes is very less as compared to in C, see graph images for comparison of process creation time in Erlang, Java and C# [here](https://msdeep14.github.io/projects/erlang_dcomputing.html)

Try out yourself in the C program set `numProcess = 100`, your system will stop responding and you need to restart the system, instead in case of Erlang set value to `200` instead of `100` and all the processes will be created within a second(didn't calculated actual time).

The comparison of Erlang processes and OS processes, I will discuss in another blogpost.
