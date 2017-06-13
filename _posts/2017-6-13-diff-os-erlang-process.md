---
layout: post
title: Erlang processes vs OS threads
---

You always studied that OS threads are very light weight as compared to processes, I'm here to introduce to processes of **Erlang** which are even lighter than OS threads.

Before you develop any misconceptions, understand this **These both are different paradigms**

## What's the reason?

    1. Erlang's processes are different from OS processes
    The processes of Erlang are created and scheduled by Erlang virtual machine(BEAM), the processes in C or Java are typical OS processes which are completely managed by operating system.

    2. Dynamic allocation
    The minimum memory allocated for a OS process is 64K, which is very large for a light weight process which is few bytes of memory. Erlang processes use dynamically allocated stacks, which initially are very small and grow afterwards according to the need.
    From [here](http://www.infoq.com/presentations/erlang-software-for-a-concurrent-world)
    [Erlang] is a concurrent language – by that I mean that threads are part of the programming language, they do not belong to the operating system. That's really what's wrong with programming languages like Java and C++. It's threads aren't in the programming language, threads are something in the operating system – and they inherit all the problems that they have in the operating system. One of the problems is granularity of the memory management system. The memory management in the operating system protects whole pages of memory, so the smallest size that a thread can be is the smallest size of a page. That's actually too big. If you add more memory to your machine – you have the same number of bits that protects the memory so the granularity of the page tables goes up – you end up using say 64kB for a process you know running in a few hundred bytes.

    3. Context switching
    Switching between Erlang processes, takes about 16 instructions and 20 nanoseconds on a modern processor. Also you often know the process pid you are switching to(example: a process receiving a message in its queue can be implemented as straight hand off from the calling process to the receiving process), so the scheduler has no role to play in this hence making it `O(1)` operation.

    To switch OS threads, it takes about 500-1000 nanoseconds, because you are calling down to kernel. The OS thread scheduler might run in `O(log(n))` or `O(log(log(n)))`, which will be noticeable if number of threads is large enough.

    Therefore, Erlang processes are faster as compared to OS threads because Erlang processes are faster and scale better because both the fundamental operation switching - it is faster and scheduling - runs very less often, [find link here](https://stackoverflow.com/a/2876788/6942060)

    The author **Joe Armstrong** built a multithreaded Apache server and his study showed that Apache maxed out just under 8K processes, while his hand written Erlang server handled 10K+ processes, [find link here](https://web.archive.org/web/20151104142503/https://www.sics.se/~joe/apachevsyaws.html)

    4. Isolation
    Erlang separates each processes's running context in terms of scheduling time, memory access and reference visibility and in doing so simplifies each component of algorithm by isolating it completely.

    In case of OS threads, they are present in same address space due to you will have to implement mutexes to avoid deadlock conditions, but since Erlang processes are completely isolated, there is no such case.


## Results

From [here](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.116.1969&rep=rep1&type=pdf) and [here](http://www.scribd.com/doc/6505089/Concurrency-Oriented-Programming-in-Erlang-by-Joe-Armstrong)

    1. We observe that the time taken to create an Erlang process is constant 1µs up to 2,500 processes; thereafter it increases to about 3µs for up to 30,000 processes. The performance of Java and C# is shown at the top of the figure. For a small number of processes it takes about 300µs to create a process. Creating more than two thousand processes is impossible.

    ![see image](https://github.com/msdeep14/How-Smartly-Erlang-Uses-Distributed-Computing/blob/master/images/process_creation_time.png)

    2. We see that for up to 30,000 processes the time to send a message between two Erlang processes is about 0.8µs. For C# it takes about 50µs per message, up to the maximum number of processes (which was about 1800 processes). Java was even worse, for up to 100 process it took about 50µs per message thereafter it increased rapidly to 10ms per message when there were about 1000 Java processes.

    ![see image](https://github.com/msdeep14/How-Smartly-Erlang-Uses-Distributed-Computing/blob/master/images/message_passing_time.png)
