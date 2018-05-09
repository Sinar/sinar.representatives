# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.representatives -t test_state_seat.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.representatives.testing.SINAR_REPRESENTATIVES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_state_seat.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a State Seat
  Given a logged-in site administrator
    and an add State Seat form
   When I type 'My State Seat' into the title field
    and I submit the form
   Then a State Seat with the title 'My State Seat' has been created

Scenario: As a site administrator I can view a State Seat
  Given a logged-in site administrator
    and a State Seat 'My State Seat'
   When I go to the State Seat view
   Then I can see the State Seat title 'My State Seat'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add State Seat form
  Go To  ${PLONE_URL}/++add++State Seat

a State Seat 'My State Seat'
  Create content  type=State Seat  id=my-state_seat  title=My State Seat


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form-widgets-IBasic-title  ${title}

I submit the form
  Click Button  Save

I go to the State Seat view
  Go To  ${PLONE_URL}/my-state_seat
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a State Seat with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the State Seat title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
