<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Vishnu Sai Bhosekar (vb434)</td></tr>
<tr><td> <em>Generated: </em> 10/23/2022 11:13:53 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/vb434" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197435436-17f77e88-c778-4a9e-bdd7-dec307cf0333.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Printing the calculated value in the output with currency format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197435587-55731f9e-c584-4192-914d-4f8526bc7781.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unchanged values<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197435817-f40c1f66-9647-4459-a6da-b9e39e8d7044.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Returning the cost using iterator in proper format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <p>Used the list iterator to access the list items and their corresponding costs<br>and used the sum method to get their sum<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197436328-51c615bc-e060-4357-acfb-433f99c662df.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for the messages that are displayed when exceptions are raised<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197436565-3d2fa7bc-5231-465d-a25c-81b34e9b8400.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entered input as cups instead of cup, which raised the invalid choice exception<br>and flow is continued, asking the user the same stage question<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197436723-f7326669-1a35-4f9d-980a-96359ccc4616.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>3 scoops of vanilla were added, after which if the user tries to<br>add any of the other possible flavour scoops, a exceeded remaining choices exception<br>is raised and the program flow is moved to the next stage<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197436987-fdfd796d-8f2c-44d1-9494-3a15ea00b2cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows the invalid payment exception, where the user is asked to enter the<br>correct amount again<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197437197-8170ec17-33b7-4c3b-bc5d-5be2b493f141.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Changed the quantity of vanilla to 1 before executing the program. After executing,<br>if the user tries to add 2 scoops of vanilla, the out of<br>stock exception is raised and a message is displayed to the user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197437495-f20fc52b-7dc8-433f-967f-5b7d1230d859.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Changed the needs cleaning variable to 1 and running the program allows 1<br>ice cream but when for second ice cream exception is raised<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <ul><li>When the quantity of any item is 0 and the user wants to<br>add that item,&nbsp;<span style="font-size: 13px;">OutOfStockException is raised.</span></li><li><span style="font-size: 13px;">After "USES_UNTIL_CLEANING" number of ice<br>creams have been delivered and the user wants another icecream,&nbsp;</span><span style="font-size: 13px;">NeedsCleaningException is<br>raised.</span></li><li><span style="font-size: 13px;">If the user inputs an invalid option, one which is not<br>part of the choices,&nbsp;</span><span style="font-size: 13px;">InvalidChoiceException is raised.</span></li><li><span style="font-size: 13px;">All ice creams have<br>max_scoops and max_toppings, if the user tries to add any more than the<br>max values,&nbsp;</span><span style="font-size: 13px;">ExceededRemainingChoicesException is raised.</span></li><li><span style="font-size: 13px;">If the user enters any value<br>other than the exact value,</span>&nbsp;<span style="font-size: 13px;">InvalidPaymentException is raised.</span></li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197910691-8f24edca-1ed6-414f-9d19-848b93f3b906.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tests 1-3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197910848-4530b0fa-1701-40d4-b2b6-b901b85c6bb5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 4,5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197911202-232cd585-128e-4fed-a2fa-4cfb276a110f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 6,7<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197911322-f1cb5027-d6b9-481d-8e72-f95c72643699.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197439095-23136d8d-0710-41b3-9b09-f79cb82fc0aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All tests passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>Test 1:&nbsp;<span style="color: rgb(220, 220, 170); background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier<br>New&quot;, monospace; white-space: pre;">test_first_selection </span>- checks if the first stage is the container<br>stage<br>Test 2:&nbsp;<span style="color: rgb(220, 220, 170); background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier<br>New&quot;, monospace; white-space: pre;">test_flavour_in_stock</span> - changing the ice cream machine item quantity to<br>1 and testing to see if the item can be added twice, OutOfStockException<br>should be raised<div>Test 3:&nbsp;<span style="color: rgb(220, 220, 170); background-color: rgb(30, 30, 30); font-family:<br>Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">test_toppings_in_stock</span>&nbsp;- changing the ice cream machine item quantity<br>to 1 and testing to see if the item can be added twice,<br>OutOfStockException should be raised</div><div>Test 4:&nbsp;<span style="color: rgb(220, 220, 170); background-color: rgb(30, 30, 30);<br>font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">test_max_scoops</span> - used a loop to add<br>a scoop max_scoops(3) times and if another scoop is added, then ExceededRemainingChoicesException should<br>be raised<br></div><div>Test 5:&nbsp;<span style="color: rgb(220, 220, 170); background-color: rgb(30, 30, 30); font-family: Consolas,<br>&quot;Courier New&quot;, monospace; white-space: pre;">test_max_toppings</span>&nbsp;-&nbsp;used a loop to add a scoop max_toppings(3) times<br>and if another topping is added, then&nbsp;ExceededRemainingChoicesException&nbsp;should be raised</div><div>Test 6:&nbsp;<span style="color: rgb(220, 220,<br>170); background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space: pre;">test_total_cost</span>&nbsp;-&nbsp;added a<br>container, some scoops, and some toppings and calculated the sum, and asserted the<br>sum to be equal to the cost calculated from the method</div><div>Test 7:&nbsp;<span style="color:<br>rgb(220, 220, 170); background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;, monospace; white-space:<br>pre;">test_total_sales</span>&nbsp;-&nbsp;added 2 ice creams, made valid payments for both, and asserted the total<br>sales to be equal to the sum of the 2 ice creams&#39; cost</div><div>Test<br>8:&nbsp;<span style="color: rgb(220, 220, 170); background-color: rgb(30, 30, 30); font-family: Consolas, &quot;Courier New&quot;,<br>monospace; white-space: pre;">test_total_icecreams</span>&nbsp;-&nbsp;added 3 ice creams, made valid payments for both and asserted<br>the total ice creams to be equal to 3, used the pytest fixture<br>second_order which has 2 ice creams delivered, and asserted the total ice creams<br>for the second order to be 2</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/9">https://github.com/vishnusaibhosekar/IS601-005/pull/9</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Learned about py tests and exception handling in python.<br>Had some trouble testing pytests<br>on VS Code, but was able to handle it using online resources.<br>Had some<br>issues with continuing the program flow after handling exceptions, and got through it<br>after refactoring the code.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/197441360-0f514348-69b9-4f7c-a773-b66af131b0be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ordered 2 ice creams - 1 cup with 1 scoop of vanilla ice<br>cream and 1 sugar cone with 1 scoop of chocolate ice cream with<br>m&amp;ms topping<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/vb434" target="_blank">Grading</a></td></tr></table>