<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Vishnu Sai Bhosekar (vb434)</td></tr>
<tr><td> <em>Generated: </em> 12/4/2022 11:56:38 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/vb434" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205538732-172ebf87-fddd-4596-8d23-0697ea2bb29e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DIAR-VB434 and Index Page shows my name, ucid and IS601 section<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205541070-8b83cca1-f54b-4d8c-9e19-7e4031b80e13.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>URL is visible and is from heroku dev<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/204161666-7d1f1692-283f-4dd2-8cf4-68eb355c637e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Both tables - Company and Employee are added to the DB. UCID and<br>DB name visible<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205541689-1f6fb539-b658-41ac-b063-23b37499daf3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code to check if uploaded file is a CSV file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205541825-c4ca6201-a6ea-4104-8a7a-4f996056c5b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Warning flash message to show no file was selected<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205541949-0b6e2dcf-fa47-4b18-a5db-c589d0e33fe7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash warning message when other file(not .csv) is uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205542296-5000bff1-97fd-4200-8e47-07e01e8d4d52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Extracted employee data should be append as a dict to the employee list,<br>Extracted company data should be appneded as a dict to the comapny list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205542614-f7fcf2f6-eca7-4088-8f78-2314aa05f561.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash message to show how many records were processed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205542614-f7fcf2f6-eca7-4088-8f78-2314aa05f561.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Should shows the proper success message, shows the proper count messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205541949-0b6e2dcf-fa47-4b18-a5db-c589d0e33fe7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash warning message when other file(not .csv) is uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205541825-c4ca6201-a6ea-4104-8a7a-4f996056c5b8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Warning flash message to show no file was selected<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205543010-6d2890a1-49f6-45e7-8131-97da6a61f462.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee data was uploaded<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205543082-61cf7417-10df-41b7-8889-c68550cb85b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Company data was uploaded<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205543890-126f67f2-e2df-4db8-9b6e-30ed932d26fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Proper INSERT query should be visible and Except block should have a user<br>friendly message flashed and a print() of the exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205544171-eaa7a39f-8e43-4bcf-95a4-875629e2bd97.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve first_name, last_name, company (id), email, first_name is required, last_name is<br>required, email is required<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205543262-bb589073-6fe3-4bb1-9b8b-72f2c6bdbb4c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first_name is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205543436-3063cbf1-0337-4ca3-9b73-065976867a0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last_name is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205543552-39811e40-3820-477b-9520-5cbc036c8506.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email is required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205544717-4cf6cf4a-1b90-4b65-a9ac-3e1c80c94ad7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Heroku URL with filled in valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205544990-276b5720-682a-49c4-8361-84d71bef3ae4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully added to DB<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205545121-82eab9cc-c1ec-4eb7-8bb5-a4307f45397e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Record added to DB<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205545706-4a3092d7-fe26-4330-b8ad-1df76b160c3d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Select query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205545829-082e185a-ae48-4166-b1f7-581a65004e99.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Checking request for args<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205545951-2562ae0a-70ed-4be3-a9b2-75f813c2620e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>appending args to query<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205546351-90efdb36-e04c-4ca2-a485-a0d703f74220.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with first_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205546416-49e58df4-e9ed-4763-8102-e166df6e933e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with last_name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205546480-eef79f83-f562-4cd9-abe9-1a0a9d00fda2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with email filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205546548-6f6360f2-6d01-443d-95b7-a23cad3d42fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with comapny filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205546723-063df92a-a322-4a7c-b79f-cb7a995d6567.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>asc filter applied on first name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205546929-17af5d2c-4faf-4e5b-b3c9-2500a3853ce8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>desc filter applied on first name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205547413-74a62d2c-b2f1-4bfb-ba72-0caea78edc43.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieves ID, firstname, lastname, company(id) from form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205547480-ab088135-8c44-4974-a1f5-de94e2e8efda.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>firstname, lastname, email is required. company id is not required.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205547699-956df473-82fb-41a6-9517-f1af1e5e67ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>UPDATE query and flash message if exception occurs<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205547834-65aed170-0e93-410f-aa54-18b3dd8645d2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query visible and Employee data passed to the render_template()<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205548194-551a3fe8-2644-4002-a58c-a395363568f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205548300-8a78a0c8-cf39-47c0-b7bf-0874949f0385.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data after edit. Successfully added.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205548474-bf004d65-420e-465d-aff4-6615cf4badaf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entry 2 before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205548538-cb1a9b39-ccaa-47e6-b3c7-b54a08cbaa64.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entry 2 before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205548636-0af75535-659e-4693-af50-6b55413619a3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated record on app<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205548692-9f4d5787-3848-4d19-8b66-02a3e5147e1b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Notice reocrd 2 with updated data<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205549361-2374b1c4-a922-4419-8ad8-3ee2708d0497.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code retrieves data sent from the form - name, address, city, state, country,<br>zip, website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205549406-fc1af7be-deb3-419e-8af5-d6b2f7b90d4e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name, address, city, state, country are required. website is not required<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205549511-db6405e8-7fc4-4bc6-afb2-3c96f7b3fe16.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Insert statement and flash message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205549671-fe542afb-202f-4091-a2a1-7206a743d404.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Heroku URL<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205549751-3a018a05-a479-4677-9779-c9f174c4afee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205549798-8732cc25-03b8-4ed5-868a-c8a391862c24.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205549853-0c8ea136-05c9-4168-a393-7e0f3a895e45.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>city address message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205549974-932209a6-f052-4c09-a73a-0d704f5fc0bd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>zip address message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205550180-b341af83-a8bf-4159-ba93-31fd8f09259c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>new data to be inserted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205550666-0a4e22b1-496b-4e94-872e-b01f718a4b73.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205550755-4c5976e9-353b-4e17-9335-9b3d062521c9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Record added to DB<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205550916-f1025209-a696-4a51-9508-062ea13b58ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should fetch id, name, address, city, country, state, zip, website, employee<br>count for the company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205550916-f1025209-a696-4a51-9508-062ea13b58ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SELECT query should fetch id, name, address, city, country, state, zip, website, employee<br>count for the company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205550979-3e72a7bc-d18f-4e18-815f-6533d083fbe5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>appending args to query<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551039-da9191a2-cb59-4872-9235-63dcb20f5e7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash error message, friendly error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551128-77393181-6188-4ab8-a0c0-329c9e619503.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551179-44ac0faa-8391-427a-abf9-4fbc582e704a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with name filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551242-9c699c41-1aa1-4946-921e-8682ae451e59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with country filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551308-d2de1532-ba14-4c92-a5f1-1b10c7f59960.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results with state filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551378-c14735d0-f446-4de0-ad34-ac6d4c76c482.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Desc filter applied on name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551438-35c73689-48af-4d89-b8bd-db2f2c43038d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Asc filter applied on name<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551517-0da1d5b4-4ff7-4db9-8aa4-d3ac3a4b250b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code should retrieve id (from request args) name, address, city, state, country, zip,<br>website from form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551557-33cb3a08-87cd-4af4-bd8c-6526f9f381cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name, adress, city, state, country is required. website is not required.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551662-60be73f2-1cb8-41fe-9925-65b8ba5f786b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update statement, select statement and flash messages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551765-9798453d-e3a9-478e-90b3-ff1af214c962.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551836-c63c8a0c-13af-467d-892d-660e7edff51a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search page before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551914-aee8d2fe-7a28-47cb-ad09-770a118546ce.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205551952-b52c6933-f099-443c-b2a1-9385124d3ff6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated data on record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205552031-3a844f3a-574b-4617-9171-65e9c9eb67bc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data before edit.. notice id 1<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205552132-b66512a6-6d3c-4512-9e8f-c2f7d17f262f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data after edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205552161-cc0f2f75-e7f1-4fca-9f00-c3a1b02059ba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Data edited on app<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/f2c037/000000?text=Partial"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205552579-78b3af84-6891-4e74-963b-fbcf4631ec8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleting employee by id, redirecting to search, all request args (minus id) are<br>passed to the redirect route and success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205552396-075f68f5-abc6-4eca-a16f-6e3fdf6c79ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>deleted employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205552246-5b30b444-4c5a-4972-9f13-9b74d4ef0d33.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>delete company by id, redirect to search<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td>Missing Image</td></tr>
<tr><td> <em>Caption:</em> (missing)</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/205539591-6b232d30-f133-4a7c-8df9-a53f9be6fda4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test cases passed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>Learnt a great deal about Flask - forms, routing, SQL Alchemy, Request Parameters,<br>Session, DataBase Connection, and validation.<br>Had issues with email validation, flask wtf and test<br>cases.<br>had issues setting up the Heroku app but was able to fix them<br>by going through the slides and video.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/vb434" target="_blank">Grading</a></td></tr></table>