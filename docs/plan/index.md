# Plan Lab

TODO: update flow, app references and screenshots
_**TODO: update flow, app references from PIZZA to EcoLogic and screenshots**_

## Introduction

TODO: add here more about Plan

## How to switch to Plan from Home Page

You can switch to Plan by either pressing "Let's go to Plan" button on its tile:

![Plan Tile lets go](../introduction/media/Loop_switch_to_Plan.png)

Or you can always switch using the central app switcher on the top left of your screen:

![Central App Switcher](../introduction/media/Loop_central_app_control.png)

## Let's go with Plan

### Select Plan application to use

If you have not set your default Plan application you will be provided with a screen with all applications you have access to.

![Plan Applications Page](media/Plan_Applications_page.png)

Set the provided app as default and presss "Let's go" to proceed.

### Welcome Page for first time users

If you have logged in the first time into Plan you will get a Welcome Screen:

![Welcome Screen](media/Plan_welcome_screen.png)

By pressing the button "Explore" a new page is shown which provides an Introduction to Plan and the used workflow model for the selected application:

![Plan Introduction page](media/Plan_welcome_introduction_screen.png)

### Use Home Button to switch to Plan Home Page

Please use the "Home" button on the left sidebar to switch to the Home page for Plan.

![Plan Home Page Button](media/Plan_Home_button.png)

This Home page will provide you some basic information and also the means to switch between Plan applications (My Applications Button on the right)

![Plan Home page](media/Plan_Home_page.png)

The explore options on this page will forward you to the Exploration page mentioned above.

### Explore the technical worflow

Pressing the button "View":

![view schema button](media/Plan_app_view_flow.png)

will open a new view to the technical details of the used workflow for the selected application.

![Schema Overview](media/Plan_app_view_details.png)

This view provides the used record types, fields, transition matrizes and more.

## Work with Boards

### Project Board

Project Boards provide a graphical Kanban style overview of worktitems.

TODO: add more text here

To open the board use the Project Board icon ![Board Icon in sidebar](media/Plan_ProjectBoard_Icon.png) on the sidebar.

The initial view is your My Board view which will show worktitems that are assigned to you. As we newly started the board is empty.
![myWork Board](media/Plan_ProjectBoard_myBoard.png)

## Create and customize a new Project

### Create a new Project

To create a new Workitem you have to click on the triangle icon on the NEW button on the top right of your screen:

![Create new Workitem Button](media/Plan_New_WorkItem.png)

![Create New Workitem List](media/Plan_New_WI_List.png)

Select Project from the List. This will create a new Record from type "Project" and will show you its Main section first to provide Name and more Details:

![New Project Main](media/Plan_New_Project_Main.png)

The name of our project is "EcoLogic", add a meaningful description too.

![Enter Project Name and Description](media/Plan_Project_New_withData.png)

### Add Releases to Project

If you have saved the Project, you need to switch back to edit mode by using the Edit Button ![Switch to Edit mode by using the Edit Button on the top left](media/Plan_Project_EDIT_Button.png)

Switch to Releases Section and press the NEW button right of the Search field:

![Project - Releases Section](media/Plan_Project_Releases_Section.png)

![Project - Releases - New button](media/Plan_Project_Releases_Search.png)

Enter "Release 1" into the Release Name and add a meaningfull description, you can change the Start and End Date if you wish.

![Project - New Release](media/Plan_Project_Releases_New_Release.png)

Press the SAVE button to save the new Release:

![Project - Save Button](media/Plan_Save_Button.png)

Please now repeat the steps to create "Release 2" which starts 1 day after "Release 1" ends and lasts for another 3 months.

In your release section you will now see your new releases:

![Project - releases list](media/Plan_Project_Releaseslist.png)

If the Save button is active for the project, please press it to save your changes!

### Add Sprints to Project

If you have saved the Project, you need to switch back to edit mode by using the Edit Button ![Switch to Edit mode by using the Edit Button on the top left](media/Plan_Project_EDIT_Button.png)

As no Sprints have been created and attached to this Project the Sprint section is empty.

![Sprint List](media/Plan_Project_Sprintlist.png)

If you have saved the Project, you need to switch back to edit mode by using the Edit Button ![Switch to Edit mode by using the Edit Button on the top left](media/Plan_Project_EDIT_Button.png)

![Create new Sprint button](media/Plan_Project_SprintList_New.png)

In the new Dialog/form enter the Sprint name "Sprint 1" and if necessary adjust the Start and End Date:

![Create new Sprint Dialog](media/Plan_Project_Sprint_New_Dialog.png)

Press the Save Button ![Project - Save Button](media/Plan_Save_Button.png) to save this new Sprint. Now the Sprint is visible in the Sprintlist of the Project:

![Sprint List with newly created sprint](media/Plan_Project_SprintList_added.png)

Repeat this steps and create more Sprints and adjust their Start and End Dates accordingly.

Example with two Sprints:

![Sprint list with two sprints](media/Plan_Project_SprintList_moreadded.png)

Please do not forget to save the project changes!

### Configure Project

If you have saved the Project, you need to switch back to edit mode by using the Edit Button ![Switch to Edit mode by using the Edit Button on the top left](media/Plan_Project_EDIT_Button.png)

Click on the sidebar on the "Configure" button/link:

![Project Configure first view](media/Plan_New_Project_Configure.png)

This screen lets you customize your project with different values for Work Item Types, Priorities, Story Points, Severities, Resolutions, Tags and Release Types. New values can be added by clicking in the white space, typing in a value and clicking the Create link that appears below. Existing values can be removed by clicking the X beside the value

In the Workitem Types remove the Hill, SubHill and Scenario work item types. You can add or remove other items based on your requirements, the new configuraiton should look like this:

![Project new configuration](media/Plan_Project_Configure.png)

Click the Save button on the lower right of the screen: ![Save Button](media/Plan_Save_Button.png)

### Add Components

If you have saved the Project, you need to switch back to edit mode by using the Edit Button ![Switch to Edit mode by using the Edit Button on the top left](media/Plan_Project_EDIT_Button.png)

Click on the sidebar on the "Component" button/link:

![Component List](media/Plan_Project_ComponentList.png)

Click on the "NEW" button to create a new component "EcoDriver":

![Create a new Component](media/Plan_Project_Component_create.png)

Save the component and create another one for "LogicDriver".

The new component list should look like this:

![Final Component List](media/Plan_Project_ComponentList_withdata.png)

Do not forget to save the project to keep the changes!

## Work with Queries

Use Queries to get a list of items you are interested on. Every user can create its own Personal Queries. If you have the role or permission set to be a Public Query Editor then you can publish personal queries as Public Queries.

### Public and Personal Queries

You can switch to the Query Editor by either Clicking on the Queries icon on the left sidebar to open the submenue:

![Queries Icon](media/Plan_Queries_Icon.png)
![Queries Menue List](media/Plan_Queries_MenueList.png)

Or when your sidebar is expanded click on Personal to create a new Personal Query:

![Queries Menue Expanded](media/Plan_Queries_Menu_expanded.png)

The Query Editor list all your queries you have access to. You can switch here between Personal and Public queries by clicking on the triangle symbol right beside the Public/Personal Query:

![Switch between Personal and Public Queries](media/Plan_QueryEditor_SwitchTypes.png)

#### create new personal query

Now let us create a simple Query to list all Projects we own. Click on the Add New Query button and select "New Query":

![Add New Query Expanded](media/Plan_PersonalQueriesAddNewExpanded.png)

This will open a Popup where you need to provide a name for your query and which record type will be queried:

![New Query](media/Plan_NewQuery.png)

Please provide a meaningful name like "My Project Query" and select the Project record type. Then Press Continue to open the Query Editor:

![Query Editor](media/Plan_QueryEditor.png)

In this Editor you can configure the fields which will be shown on the result. It is also possible to add fields from related record types like Releases or Sprints. In this example we will keep it Simple and add only the Tagslist to our Result set.

Scroll down on fields list to Tags and press the arrow to add it to your result field view:

![Add Field to Result list](media/Plan_QueryEditor_AddField.png)

In the results field view you can change the ordering of the fields, set the sort order and more. Every field reveals a three dot inline menue for modification of these parameters or if you added it by mistage to remove this field from this list.

![Three Dots of a field](media/Plan_QueryEditor_FieldThreeDots.png)

Now let us do a dry run and see the results. Press the Run button on the bottom right of your screen to run and have a look at the result:

![Run the Query](media/Plan_QueryRun.png)
![Query Result](media/Plan_QueryResult.png)

Use the "Back to Edit" link to return to the Query Editor to add aditional fields or change the query:

![Back to Edit](media/Plan_QueryEditor_runBackToEdit.png)

We need to add a Filter on our Query so that only our own items are selected. This can be done by clicking on the Query Filter link on the top above the field list:

![Query Filter](media/Plan_Queries_Filter.png)

In this view select Owner from the field list and press the arrow button to add it to the Filter Criteria, then you need to change the value to "Current User":

![Set Filter to use Current User](media/Plan_Queries_Filter_CurrentUser.png)

NOTE: you could have selected your own username from the list, but to if you want to publish this query, you can use the generic "Current User" which will automatically use the username of the logged in user.

We are now finished with setting up our query. Press Save and Close on the bottom left:

![Query Save and Close](media/Plan_QuerySaveClose.png)

If you want to save and go on with editing use the Save button. It can be also used for saving your query under a new name too:

![Query Save Menue](media/Plan_QuerySaveExpanded.png)

#### Public Queries

Have a look at the available Queries in the Public Queries list and try them out.

## Conclusio

Congratulations! You have finished the Plan lab and have got a short overview of its capabilities.
