<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Vishnu Sai Bhosekar (vb434)</td></tr>
<tr><td> <em>Generated: </em> 12/22/2022 11:00:15 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-3-shop-project/grade/vb434" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
Video Presentation for the final project of IS601

[![YouTube Video](https://img.youtube.com/vi/jq14viS3NoA/0.jpg)](https://www.youtube.com/watch?v=jq14viS3NoA)
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209264618-401ce25e-1094-415c-8667-b891d6b86401.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Orders table with valid data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209264678-62bd1626-5994-4cba-bbe7-2db08943ec07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>OrderItems table with validate data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209264831-45106e13-bb94-4448-9909-d89ab1077e74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before purchase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209264907-7870145c-17ac-4bf3-8658-33aea7652d1e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After successful purchase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209264831-45106e13-bb94-4448-9909-d89ab1077e74.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before purchase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209265441-78224fc1-2787-4bb9-b4d0-bf8ad63f73d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entering amount 0<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209266077-1eae4748-e89b-4408-8e53-20f11d5eb8d5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to check if qty selected is present in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209266127-27241402-1103-4260-b60a-34e4d1e4c63a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to validate the order process<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209266335-7ba6edc1-abb1-4c1b-87a9-138b5b9b1296.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Empty form fields validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209266389-681d4e16-8ece-4b16-9543-09149122ac8a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Incorrect amount error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <p>The order process form is displayed to the users when they fill in<br>the order details. These values are passed as params to the /purchase route<br>where the values are validated with the database table values and if there<br>is a mismatch, error messages are displayed<br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209266740-367a0967-3a15-4a1d-bdaa-b2a805a6a73a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order details from the Order table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209266791-46080c4e-0d5d-4bc5-8679-e9f81cb337ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Order details from the OrderItems table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209266669-cf1dfada-46c4-4156-b343-ef957c31d7e7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Thank you message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <p>Two queries are run from the same route, the respective results are stored<br>in different variables and passed to the UI to be displayed in the<br>form of tables<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209266975-da07a689-a1b7-4e4b-b7b1-3a054c3051f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing purchase history for a user, list item can be clicked to<br>view the full details in the Order Details Page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209267095-0252bf1a-fa63-4aa0-9c5e-aea4333b6c73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Full details in the Order Details Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209267095-0252bf1a-fa63-4aa0-9c5e-aea4333b6c73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing full details of a purchase (Order Details Page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <p>Every order is added to the orders table with a unique order id,<br>these values are retrieved after the order table and product table are joined<br>and displayed on the UI in tabular form.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209267535-8088845e-f65a-4752-af9d-c1bc6aa0ce87.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing purchase history from multiple users<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209267592-35a95be7-e55a-404b-b03e-87e2f45fe665.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>List item can be clicked to view the full details in the Order<br>Details Page, results should show the username of the person who made the<br>Order <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209267592-35a95be7-e55a-404b-b03e-87e2f45fe665.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing full details of a purchase (Order Details Page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <p>Every order is added to the orders table with a unique order id,<br>these values are retrieved after the order table and product table are joined<br>and displayed on the UI in tabular form.<br>The logic is mostly similar to<br>how the users see the order details page, except that the user id<br>is passed when the admin tries to see the order details, whereas the<br>customer&#39;s id is retrieved from the current user&#39;s data.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209268079-3f1c3831-2010-4809-8278-bbab41f6e3a4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The checkout button takes the user to the payment page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>Had to use joins on multiple tables are retrieve values from the<br>newly joined table.<br>- Had to brush up on joins and used w3 schools<br>as reference.<br>- Learnt how e-commerce websites are developed on a microscopic level, all<br>the validations that are needed to process a customer&#39;s order.<br></li><br></ul><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-3-shop-project/grade/vb434" target="_blank">Grading</a></td></tr></table>