'''

Phase Six: Form Support


1) Add a new html file into views called "create_post.html"

   - add a html form to the page

   - the form has inputs,  post_name and post_text

   - add a submit input

   - This doc has good guidlines for forms: http://learn.shayhowe.com/html-css/building-forms/

2) Add a new action for 'blog/new' tied to blog_new

   - renders the new_post.html

3) Update the form in create_post.html to <form action="/blog/create" method="post">

4) Add a new action for 'blog/create' tied to blog_create

   - have it return blog_index_page

5) Refactor the controller functions blog_index,blog_create... 

   - to accept the body of the http request

6) Write a new helper function called process_form 
 
   - it takes the body and take the form line from the end of body

   Ex: 'post_name=test&post_text=test'

   - and returns a hash {'post_name':'test','post_text':'test'}

7) Use proccess_form in blog_create to create a new row in the db using BlogModel

8) Last redirect to blog/<new id>

'''


