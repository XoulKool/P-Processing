# P-Processing
The test to follow after Non Parallel Processing

Once again this test requires you to have the same five terminals as in the previous test - That is the Pica8, grnlntrn, server5, server6, and server7.  Instructions for sshing into the terminal were given in the last tests, read me so please look at that.  Again, remember to delete any flows that have been created by prior tests in the Pica8 by using the commands specified in the last two tests on the Pica8 terminal.  Also, this test uses OpenFlow 1.0 so make sure the Pica8 switch is set for this version using the command specified in the last two tests.

Note that in this test the goal is to time the transfer of two large data files in parallel, that is sending two different files through the same port on the Pica8 switch at one time and measuring how much faster this is than round-robin scheduling transfers.  Keep in mind your transfer files will already need to be created and the two listening servers must know the name of these files.

The first part of the test invloves starting up the two listening servers on servers 5 and 7.  Do this on server 5 with command

``
