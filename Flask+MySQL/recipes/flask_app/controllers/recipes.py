# Import necessary modules and classes
from flask_app import app
from flask import request, render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

# Route to display the form for creating a new recipe
@app.route('/recipes/new')
def new_recipe():
    # Check if the user is logged in
    if 'user_id' in session:
        # Render the template for creating a new recipe
        return render_template("new_recipe.html")
    # If not logged in, redirect to the home page
    return redirect('/')


# ========================== CREATE ===============================

# Route to handle the creation of a new recipe
@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    # Validate the form data
    if Recipe.validate(request.form):
        # Create a dictionary with form data and the user_id from the session
        data = {**request.form, 'user_id': session['user_id']}
        # Add the new recipe to the database
        Recipe.add_recipe(data)
        # Redirect to the dashboard after successful creation
        return redirect('/dashboard')
    # If form validation fails, redirect back to the new recipe form
    return redirect('/recipes/new')



# ========================== DELETE ===============================


# Route to handle the deletion of a recipe
@app.route('/recipes/<recipe_id>/destroy/')
def delete_recipe(recipe_id):
    # Check if the user is logged in
    if 'user_id' in session:
        # Delete the recipe with the specified recipe_id
        Recipe.delete({'id': recipe_id})
    # Redirect to the dashboard after deletion
    return redirect('/dashboard')


# ========================== EDIT ( render route) ===============================


# Route to render the form for editing a recipe
@app.route('/recipes/<recipe_id>/edit')
def edit_recipe(recipe_id):
    # Check if the user is logged in
    if 'user_id' in session:
        # Retrieve the details of the recipe with the specified recipe_id
        one_recipe = Recipe.get_by_id({'id': recipe_id})
        # Render the template for editing a recipe with the retrieved data
        return render_template("edit_recipe.html", recipe=one_recipe)
    # If not logged in, redirect to the home page
    return redirect('/')


# ========================== EDIT ( action route) ===============================


# Route to handle the update of a recipe
@app.route('/recipes/<recipe_id>/update', methods=['POST'])
def update_recipe(recipe_id):
    # Validate the form data
    if Recipe.validate(request.form):
        # Update the recipe with the new form data
        Recipe.edit_recipe(request.form)
        # Redirect to the dashboard after successful update
        return redirect('/dashboard')
    # If form validation fails, redirect back to the edit recipe form
    return redirect('/recipes/' + str(recipe_id) + '/edit')



# ========================== GET ONE ( BY ID) ===============================


# Route to display details of a specific recipe by its ID
@app.route('/recipes/<int:recipe_id>')
def one_recipe(recipe_id):
    # Check if the user is logged in
    if 'user_id' in session:
        # Retrieve details of the logged-in user
        user = User.get_by_id({'id': session['user_id']})
        # Retrieve details of the recipe with the specified recipe_id
        one_recipe = Recipe.get_by_id({'id': recipe_id})
        # Render the template to display details of the recipe
        return render_template('one.html', recipe=one_recipe, user=user)
    # If not logged in, redirect to the home page
    return redirect('/')
