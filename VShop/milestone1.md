<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Vishnu Sai Bhosekar (vb434)</td></tr>
<tr><td> <em>Generated: </em> 12/22/2022 8:58:35 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/vb434" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248178-db570dee-eb53-4358-b646-84a0a347eeb9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248314-a119b7db-8450-422c-a75f-2b4f5c30f6f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248388-7a295cf4-8348-42dd-96d9-4ba2632fd8b1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Passwords do not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248632-a81f91c9-4734-490e-a7b6-35526b863a58.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Users db already contains admin with email <a href="mailto:&#97;&#x64;&#109;&#105;&#110;&#x40;&#103;&#109;&#x61;&#x69;&#108;&#x2e;&#99;&#x6f;&#x6d;">&#97;&#x64;&#109;&#105;&#110;&#x40;&#103;&#109;&#x61;&#x69;&#108;&#x2e;&#99;&#x6f;&#x6d;</a><br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248575-bb86807f-7a76-434d-9dcd-0088ab847cd1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email not available validation (already registered) - <a href="mailto:&#97;&#100;&#x6d;&#105;&#x6e;&#64;&#x67;&#x6d;&#97;&#x69;&#x6c;&#x2e;&#99;&#x6f;&#x6d;">&#97;&#100;&#x6d;&#105;&#x6e;&#64;&#x67;&#x6d;&#97;&#x69;&#x6c;&#x2e;&#99;&#x6f;&#x6d;</a> already exists in table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248510-4a5300f5-a90d-44b5-b0e6-84534c820209.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username not available validation (username is taken) - admin already exists in table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248773-252fb1d0-83c8-4fbb-b5e9-7986ded25cdf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Form with valid data filled in before the form is submitted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248871-5f678a13-cac2-4b65-b030-d61abc91f2f6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully registered user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248928-862bd5f7-0fbb-4520-aa20-37c4d8ca20cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid user data from Task 1 present in this screenshot - highlighted which<br>row it is in the Users table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>- I used WTforms for form generation and validation. The form submission will<br>attempt to deliver data to our Python POST route, which will extract the<br>data and run an insert query to our sample table.</div><div>- WT-form validators are<br>used to validate data both in front &amp; backend, the username is validated<br>to be of length between 2 &amp; 30 characters and it shouldn't be<br>previously used by another user, email validation is done using an email validator.</div><div>-<br>Password &amp; confirm password should both be the same and should be of<br>a length of 8, This is validated using wtforms validators and it is<br>stored in the database after hashing it using the bcrypt hashing algorithm.</div><div>- Email,<br>username, and hashed password are stored in the users table.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209249431-c3a1c0cf-d287-4cb2-9535-ce76332e0d34.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation based on non-existing user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209249471-edfea023-09a3-464f-a476-2d9c4d4c2a48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch validation (doesn&#39;t match what&#39;s in the DB)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209249557-a299c642-158f-4524-ab28-ba82619eeb67.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>- The form is handled with wtforms and each field has its own<br>validation. The form can only be submitted successfully once all the fields have<br>met the requirement.</div><div>- Validation is done with the help of wtforms validators which<br>work for both front-end and back-end.&nbsp; The "Email or Username" field accepts either<br>email or username and is validated based on the input. If the username<br>or email is not present in the database then a flash message saying<br>"Invalid User" is displayed.</div><div>- If the username matches but not the password then<br>a flash message saying "Invalid Password" is displayed.</div><div>- The password entered is matched<br>with the hashed password which is already present in the database. A function<br>bcrypt.check_password_hash() does this matching with the help of salt value.</div><div>- Both password and<br>email or username are matched with the tuples in the database from the<br>users table which holds the data while registering.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209250197-9e2c8245-d5b2-4794-9bdc-ca24f3c0ff5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing user successfully being logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209250271-5e7a66f8-02d6-49bb-a59f-d23bf6dd69d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing Unauthorized Access when user is not logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div>- I used the flask_login package to work with the user session &amp;<br>manage it, In our main.py.<br>- I used LoginManager, which handles our user session<br>and provides helpful utilities.</div><div>- Since I am using an app factory I’ll define<br>a variable for login_manager outside of the factory, then inside the factory, use<br>its init_app() method to associate the app.</div><div>- Next, inside the app factory I<br>used the user_loader decorator, this will run a process to look up a<br>user by id.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209250271-5e7a66f8-02d6-49bb-a59f-d23bf6dd69d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Message showing user not being logged in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209251579-71dfa000-79ce-4576-a933-e18aeda91670.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>&quot;Permission denied&quot; message shown for not having proper role or permission<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209251247-5cbecc1f-cbe5-4b83-bf0e-aa6ae3003759.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Role Table with data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209251348-214fbc72-8930-4144-baf9-886ea8908510.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User_id 1 with username &quot;admin&quot; is admin<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>- Login-protected pages are protected with the @login_required decorator provided by flask_login.</div><div>- This<br>triggers the user_loader for each page request.</div><div>- The user will be loaded from<br>the session if exists to avoid repeated database calls.</div><div>- If not present in<br>the session then it loads from the database.</div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div>- Similar to the login-protected page, here we use the @admin_permission_require function for<br>roles, and permissions.</div><div>- If the user is not an admin, we raise a<br>403 exception and display a 403 HTML page saying permission denied.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209252048-5a050254-14e6-4b96-a04d-4c06814d1ae4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Landing page with a sweet message :)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209252127-d7b9fcbe-e65e-451f-a0b8-5fb5d9192a9c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Stylized forms - centered and aligned neatly<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209252250-e148e716-7c9e-451c-a0cf-963f8d4e7fee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Table with neat orientation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <div>- I have followed a light theme for the website with a dark<br>header nav and footer.</div><div>- Chose a sample navigation from bootstrap where the login,<br>register, and log out will be to the right extreme separated from the<br>main nav.</div><div>- I have given some inline styles to order the filter and<br>apply the roles layout.<br></div><div>- I have given some inline styles to tables.<br></div><div>- I<br>have chosen a card layout for all the forms with limited width so<br>that the text fields will be within the required length.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248510-4a5300f5-a90d-44b5-b0e6-84534c820209.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username not available message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209248314-a119b7db-8450-422c-a75f-2b4f5c30f6f9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password not long enough message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209250271-5e7a66f8-02d6-49bb-a59f-d23bf6dd69d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized access message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div>- For the HTTP server error messages like 401, 403, and 404 I<br>have created separate pages with custom and user-friendly messages being displayed.</div><div>- If any<br>of those errors occur it will be redirected to render its respective HTML<br>page.</div><div>- For duplicate entry exceptions which occur for username or email, I extracted<br>the field name from the exception message and displayed a flash message that<br>it</div><div>is not available.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209253078-fdefaa0f-3a3a-4929-9267-be5bb6a8bf94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email and username prefilled properly<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <div>- When the profile page is loaded, the user id is fetched from<br>the current_user.</div><div>- With that user id email and username of that user are<br>fetched from the database and populated to the respective fields.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209253547-99f95af7-759c-4281-b008-e6ea4c10a13d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged in as user &quot;vishnusai&quot; and tried to fill username as admin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209254294-c362111b-b1f8-4102-8e1b-98f984f1ae25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid email message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209254451-0c318520-71c4-43b4-a8db-4d8e00d5fd2a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid username message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209254053-30868cde-7103-4833-81a3-9a0781510288.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209254110-2a9ae12d-bec5-4c43-a541-ff299dbc8943.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch error<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209253827-ab805c3c-dc53-471a-b8c1-1f785a5dd949.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User friendly warning message being displayed saying username not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209253925-472e5f41-db3f-49af-b110-30ba0d796afa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>User friendly warning message being displayed saying email not available<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209254721-f6609b4d-f198-4685-9593-4e039983f2b0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before editing <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209254780-8ba8cc94-bf35-4424-bbf7-0b1cef0a5b44.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updating value in UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209254813-2a5bdd57-1fda-4184-a768-a3839ee5c352.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Profile saved<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209254928-7a5880d0-8af0-4e33-8f4a-49db5f8757b6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated value in db<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div>- The code first checks if it is a POST request, if it<br>is, then it checks if current_password, password &amp; confirm are given, then it<br>retrieves the password from the users table, then the current password &amp; pwd<br>from DB are compared to check if they are the same or not,<br>if they are not same we will raise an invalid password error, if<br>they are the same then the new password is hashed &amp; updated in<br>the database.</div><div>- Then the username and email are updated in the database and<br>a flash message "saved profile" is displayed.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>- I got a chance to learn about user login sessions, login/registration systems,<br>and authentication systems and was able to integrate the DB utility and manage<br>the website by storing and retrieving the data from the database.</div>- Faced "jinja2.exceptions.UndefinedError:<br>'flask_login.mixins.AnonymousUserMixin object' has no attribute 'has_role'" this error while checking for the user<br>role to populate the user-specific navigation link for admin. Figured out that it<br>is being caused as I was checking for the current user before checking<br>if the user is authenticated. Resolved it by adding an authentication check before<br>checking the role.<br><div>- Learnt about deploying to Heroku. Faced an issue with the<br>deployment of the Heroku app but later resolved it with the suggestion of<br>the professor.<br></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/vb434" target="_blank">Grading</a></td></tr></table>