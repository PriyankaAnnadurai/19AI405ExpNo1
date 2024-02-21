<h1>ExpNo 1 :Developing AI Agent with PEAS Description</h1>
<h3>Name: PRIYANKA A</h3>
<h3>Register Number: </h3>


<h3>AIM:</h3>
<br>
<p>To find the PEAS description for the given AI problem and develop an AI agent.</p>
<br>
<h3>Theory</h3>
<h3>Vacuum Cleaner agent:</h3>
<p>The VacuumCleanerAgent is a Python class that simulates the behavior of a basic vacuum cleaner in a two-location environment ("A" and "B"). The agent can perform four actions: move left, move right, suck dirt, and do nothing. Its state includes the current location and dirt status in each location. The agent's initial state is at location "A" with no dirt. Actions like moving and sucking dirt can change its state, and the print_status method displays the current location and dirt status. This agent provides a foundation for simple vacuum cleaner simulations and can be adapted for more complex scenarios.</p>
<hr>
<h3>PEAS DESCRIPTION:</h3>
<table>
  <tr>
    <td><strong>Agent Type</strong></td>
    <td><strong>Performance</strong></td>
     <td><strong>Environment</strong></td>
    <td><strong>Actuators</strong></td>
    <td><strong>Sensors</strong></td>
  </tr>
    <tr>
    <td><strong>Vacuum Cleaner agent</strong></td>
    <td><strong>Cleaning Dirt</strong></td>
     <td><strong>Rooms, floor</strong></td>
    <td><strong>Dirt,Cleaning</strong></td>
    <td><strong>Location, Sensing Dirt</strong></td>
  </tr>
</table>
<hr>
<H3>DESIGN STEPS</H3>
<h3>STEP 1:Identifying the input:</h3>
<p>Location.</p>
<h3>STEP 2:Identifying the output:</h3>
<p>move_left: Moves the agent to the left if it is currently at location "B.". move_right: Moves the agent to the right if it is currently at location "A." suck_dirt: Sucks dirt in the current location if there is dirt present. After sucking dirt, the dirt status in that location is updated to indicate cleanliness. do_nothing: Represents a passive action where the agent remains idle</p>
<h3>STEP 3:Developing the PEAS description:</h3>
<p>PEAS description is developed by the performance, environment, actuators, and sensors in an agent.</p>
<h3>STEP 4:Implementing the AI agent:</h3>
<p>Clean the room and Search for dirt and Suck it.</p>
<h3>STEP 5:</h3>
<p>Measure the performance parameters: For each treatment performance incremented, for each movement performance decremented</p>
