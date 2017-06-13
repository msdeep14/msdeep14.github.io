---
layout: post
title: Process creation in C vs Erlang
---

Process is the running instance of program, so to execute any program we need to create a process, there are various defined proceduces depending on language for creation of process.

For example in C, we use `fork` and `spawn` in Erlang.

If you are a computer science student, you might have come across the term `fork` in your operating systems course, as far as **Erlang** is concerned you might not have heard about it.

Before I go to the process creation in both the languages, I will encourage you to read something about Erlang on internet.

## Process creation in C

```#include <stdio.h>   /* printf, stderr, fprintf */
#include <sys/types.h> /* pid_t */
#include <unistd.h>  /* _exit, fork */
#include <stdlib.h>  /* exit */
#include <errno.h>   /* errno */
int child = 0, parent = 0;
int main(void){
   for(int i=0;i<10;i++){
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
}```