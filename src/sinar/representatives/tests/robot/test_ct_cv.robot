# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.representatives -t test_cv.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.representatives.testing.SINAR_REPRESENTATIVES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_cv.robot
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

Scenario: As a site administrator I can add a CV
  Given a logged-in site administrator
    and an add CV form
   When I type 'My CV' into the title field
    and I submit the form
   Then a CV with the title 'My CV' has been created

Scenario: As a site administrator I can view a CV
  Given a logged-in site administrator
    and a CV 'My CV'
   When I go to the CV view
   Then I can see the CV title 'My CV'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add CV form
  Go To  ${PLONE_URL}/++add++CV

a CV 'My CV'
  Create content  type=CV  id=my-cv  title=My CV


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form-widgets-IBasic-title  ${title}

I submit the form
  Click Button  Save

I go to the CV view
  Go To  ${PLONE_URL}/my-cv
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a CV with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the CV title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
