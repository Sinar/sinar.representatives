# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.representatives -t test_issue.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.representatives.testing.SINAR_REPRESENTATIVES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_issue.robot
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

Scenario: As a site administrator I can add a Issue
  Given a logged-in site administrator
    and an add Issue form
   When I type 'My Issue' into the title field
    and I submit the form
   Then a Issue with the title 'My Issue' has been created

Scenario: As a site administrator I can view a Issue
  Given a logged-in site administrator
    and a Issue 'My Issue'
   When I go to the Issue view
   Then I can see the Issue title 'My Issue'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Issue form
  Go To  ${PLONE_URL}/++add++Issue

a Issue 'My Issue'
  Create content  type=Issue  id=my-issue  title=My Issue


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form-widgets-IBasic-title  ${title}

I submit the form
  Click Button  Save

I go to the Issue view
  Go To  ${PLONE_URL}/my-issue
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Issue with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Issue title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
