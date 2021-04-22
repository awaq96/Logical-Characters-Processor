
In this program we will design a logical characters processor. The processor will receive a series of characters as input and produce a series of characters as output. The processor may house any number of processing blocks. Not all blocks that are available may be used when creating a processor. Also, a block may be used more than once. The order in which the blocks are used may also vary.
                                                            

		...input... -> | block1 block2 block3 ... | -> ...output...
                           Processor

Let's discuss some examples of blocks and then revisit the processor.

1. UpperCaseConverter Block
	Given a character, this block will send out or return the character in uppercase.

2. LowerCaseConverter Block
	Given a character, this block will send out or return the character in lowercase.
	
3. Multiplier Block
  Given a character, this block will send out or return two of the same character. For example, if it received 'a', it will produce 'aa'. If it receives '1', it will produce '11'.

4. z-blocker Block
  Given a character, if the character is a lowercase 'z', this block will not return or produce anything. If it is any other character, it will produce the given character as output. For example, 'a' will result in an output of 'a'.

5. Z-blocker Block
	This block will not return or produce an output if the character given is an uppercase 'Z'.
	
6. k-blocker Block
   This block will not return or produce an output if the character given is lowercase 'k'.

The program should allow end users to create other similar blocks they like.

The end user should be able to create a processor using any series of blocks.

For example, a user may create a processor with the following series of blocks:
	UpperCaseConverter - z-blocker - LowerCaseConverter
	
After creating this processor, if a user were to send the following series of characters as input:

	11abcdabcdabcdzzaazzabcd

it will return the following output:

	11abcdabcdabcdaaabcd

In addition to designing a few sample blocks and the processor, we will create a console based driver program.
	
Design the program in such a way that:

1. A user can specify the blocks available for use before the program starts. This should include pre-defined blocks and user created blocks.

2. The user can specify, through a file, the blocks they'd like to use and the order or sequence in which they'd like to use them.

