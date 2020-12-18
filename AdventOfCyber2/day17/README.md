# day17 - ReverseELFneering

**radare2**

:heavy_exclamation_mark: there are multiple differences between a linux system and a macOS 

First we log into the deployed machine, the creds are given.
There are two files, we start by the `file1`.

```
r2 -d ./file1
```

![file1](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day17/file1.png)

It will open the binary in debugging mode. Once the binary is open, one of the first things to do is ask __r2__ to analyze the programe by typing `aa` (process can take up to 10 minuts).

![file1-aa](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day17/file1-aa.png)

**We can ask for help by typing `?` or for a more specific exmeple : `a?`.**

Once the analysis is complete, we want to know where is the `main`, meaning where we can start analysing from (most programs have a main).

To find a list of functions, run `afl ( | grep main)`:

![file1-afl](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day17/file1-afl.png)

We can see that here, ther is a main. We can see looking at it using `pdf @main` (_p_rint _d_issamebly _f_unction).

![file1-pdf](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day17/file1-pdf.png)

We want to analyze the program from the 4th instruction, that we can do by typing `movl $4`.
Then we have to use __breakpoints__ to analyse it step by step. We can set a breakpoing by using the command `db`; in this case it would be `db 0x00400b55` to only check the first lines. We can check if the breakpoint is set by looking at `pdf @main`, there'll be a little `b` where the breakpoint is set.

![file1-b](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day17/file1-b.png)

Running `dc` will execute the program until we hit the breakpoint.
So from now on, we have to set appropriate breakpoints, use `ds` to move through intructions and check the values of register and memory. If we make a mistake, we can use `ood` to reload the program.

![file1-dc](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day17/file1.png)

Then we can look the value of a variable by typing `px @ <variable>`. Here we see its `0`for the moment (first byte).

![file1-px](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day17/file1.png)

Then after running the next instruction (using `ds`), we see the value has changed to `0400`.

![file1-ds](https://github.com/oghobhainn/TryHackMe/blob/main/images/adventofcyber/day17/file1.png)

**Then, boy, it goes nuts. Don't go the assembly way, it's too dark and full of secrets.**
