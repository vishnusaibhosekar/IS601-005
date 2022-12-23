<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Vishnu Sai Bhosekar (vb434)</td></tr>
<tr><td> <em>Generated: </em> 12/22/2022 10:18:42 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-2-shop-project/grade/vb434" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209256565-26bc6937-153b-4d10-b7f1-de0c6203dce5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Contains 11 items before adding new item<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209256726-520d4f6a-31d5-42f6-9ed2-50e19f0c1f92.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid data filled in<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209256763-b0892f7f-0e1c-45c8-b862-e64b050a6dd5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully added to database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209256843-ec55c84f-adf7-4a51-98c2-b92ea665d4ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entry in db table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209256843-ec55c84f-adf7-4a51-98c2-b92ea665d4ed.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entry in db table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209256909-69cc0505-4278-46ee-a96d-12156dde633e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Products table clearly showing the columns<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>The values entered by the admin are passed as parameters to an<br>insert statement on form submit.<div>- The corresponding values are added to the table.</div><br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209257104-99e3e5f1-ab63-456c-b72f-eede4ab3c2ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shop page showing 10 items without filters/sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209257196-3bf361cd-c64d-4eca-b9c0-2e5a4d4c96b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Entered ch in the Product name text field, sorted by price descending<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209257513-4d854cb1-9abd-4b55-abbd-aae1ea96a867.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filter/sort logic from the code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>The filters are added as a form and every time user hits<br>the filter the values selected by the user are passed as parameters and<br>those parameters are appended to a select query which returns rows after applying<br>the conditions.<div>- The results obtained from the query are displayed in the UI<br>after being added to the HTML fields.</div><br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209256909-69cc0505-4278-46ee-a96d-12156dde633e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin/Shop Owner Product List<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>A simple query to select all the columns from the products table<br>is run and the results are sent to HTML where they are added<br>to the HTML table and fields.<br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209258434-ac0376c3-1c1b-4498-b424-6dec42348788.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209258566-4d741523-7534-40c8-b9f6-2cddd0c5867a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Product Details<br>Page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209256909-69cc0505-4278-46ee-a96d-12156dde633e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot showing the edit button visible to the Admin on the Admin Product<br>List Page (The admin page)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209259168-3d18737a-71d1-460d-bb23-bf7fc7a72355.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before updating the first entry - Chair<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209259228-56eaa791-d5c1-48f6-a475-85903db76f48.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Editing the name using UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209259294-f9be6aa8-1324-4390-9919-35ae009a661e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully updated the entry<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209259367-b6caee5c-7b36-4cad-93c1-5e335bfd3fdd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Value updated in db table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209259421-9ab6334f-5026-4bd5-8233-14ebef9e5874.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated value displayed on Shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>The values entered in the form are passed as parameters to an update<br>query which updates the entry in the DB table.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209260649-63112844-27e9-4e0b-a5ed-b498fcc162be.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The &quot;Shop&quot; button on the navbar shows displays all the products<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209260813-a3c57bd6-bd84-4b4f-87b7-2148cfc3c5aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Results in the products being displayed as cards with their names, costs, and<br>respective stock values<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>The button redirects to /shop route.<br>- The route has code to run<br>a query to retrieve values from the products table.<div>- The result of the<br>query is stored and passed to the view as parameters which are updated<br>in the card HTML fields while the page is rendered.</div><br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209261212-6c34a7ab-7d68-467b-b661-292bdd79bf7e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the success message of adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209261276-7a212aa2-ad6f-4fcf-a9ed-a805e8976a5f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the error message of adding to cart (i.e., when not logged<br>in)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209261329-f35c2220-cf45-42d3-a01f-ee41f3be4d46.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of the Cart table with data in it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>1 cart per user for VShop<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>When a user adds a product to the cart, it is stored<br>in the cart table along with the user id.<div>- When a user logs<br>in, his user id is stored in the current_user() and this user id<br>is accessed as and when required.</div><div>- When the user clicks on the cart<br>page, all the values from the cart table associated with that user id<br>are retrieved and displayed on the UI in a tabular form.</div><div>- Simple math<br>logic is applied and the subtotal of the cart is calculated.</div><br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209261856-82eafa43-09cd-4e2a-8346-280371b0b26e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows subtotal of each line (line subtotal) should add up properly based on<br>quantity and unit price, shows cart total (should add up properly), link to<br>product details page for each product<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209262120-6d3bbbc9-a595-419b-8359-e11dfcfec048.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>When a user adds a product to the cart, it is stored<br>in the cart table along with the user id.<div>- When a user logs<br>in, his user id is stored in the current_user() and this user id<br>is accessed as and when required.</div><div>- When the user clicks on the cart<br>page, all the values from the cart table associated with that user id<br>are retrieved and displayed on the UI in a tabular form.</div><div>- Simple math<br>logic is applied and the subtotal of the cart is calculated.</div><br></li><br></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209262440-444ed132-0191-4bc1-88bd-27595b18065b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before updating value in cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209262493-86965d1d-10c9-433a-9eb8-f2fc5b363cb8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After updating value in cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209262440-444ed132-0191-4bc1-88bd-27595b18065b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209262667-de577f11-17f8-4c72-9a6b-0d9162280fee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before clicking update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209262704-5348c8ad-48cf-485c-9772-a57d96a7467a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After setting val to 0 and clicking update - deletes the item from<br>cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209262822-7787fba3-19a1-4c77-b9f6-6fc708430e1c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Set the min value to 0, so the user cannot select a negative<br>value<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>Added the min attribute to the number input field and set it to<br>0 so the so the user cannot set a value less than 0<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209262988-2a5cd124-5bfe-488d-8d3e-7c3c16c10d07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209263031-8dfa7d93-2209-44c4-ab11-a64cb8f48e46.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After delete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209263085-616b3ecd-9f49-4fc4-ba20-f4a8fcc3c7f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before clearing cart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/85636187/209263220-3fc64193-ef9e-48cf-8488-5235f480e23f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After clearing cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>All the entries associated with the user id in the cart table are<br>deleted.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/vishnusaibhosekar/IS601-005/pull/51">https://github.com/vishnusaibhosekar/IS601-005/pull/51</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Faced an issue while restricting the value of the product qty to be<br>greater than -1. Did some research and found the min attribute to the<br>number input field.</div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://vb434-finalproject-prod.herokuapp.com/">https://vb434-finalproject-prod.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-2-shop-project/grade/vb434" target="_blank">Grading</a></td></tr></table>