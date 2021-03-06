# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.representatives -t test_parliamentary_seat.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.representatives.testing.SINAR_REPRESENTATIVES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_parliamentary_seat.robot
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

Scenario: As a site administrator I can add a Parliamentary Seat
  Given a logged-in site administrator
    and an add Parliamentary Seat form
   When I type 'My Parliamentary Seat' into the title field
    and I submit the form
   Then a Parliamentary Seat with the title 'My Parliamentary Seat' has been created

Scenario: As a site administrator I can view a Parliamentary Seat
  Given a logged-in site administrator
    and a Parliamentary Seat 'My Parliamentary Seat'
   When I go to the Parliamentary Seat view
   Then I can see the Parliamentary Seat title 'My Parliamentary Seat'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Parliamentary Seat form
  Go To  ${PLONE_URL}/++add++Parliamentary Seat

a Parliamentary Seat 'My Parliamentary Seat'
  Create content  type=Parliamentary Seat  id=my-parliamentary_seat  title=My Parliamentary Seat


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form-widgets-IBasic-title  ${title}

I submit the form
  Click Button  Save

I go to the Parliamentary Seat view
  Go To  ${PLONE_URL}/my-parliamentary_seat
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Parliamentary Seat with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Parliamentary Seat title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
