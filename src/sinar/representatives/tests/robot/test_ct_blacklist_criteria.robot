# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.representatives -t test_blacklist_criteria.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.representatives.testing.SINAR_REPRESENTATIVES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_blacklist_criteria.robot
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

Scenario: As a site administrator I can add a Blacklist Criteria
  Given a logged-in site administrator
    and an add Blacklist Criteria form
   When I type 'My Blacklist Criteria' into the title field
    and I submit the form
   Then a Blacklist Criteria with the title 'My Blacklist Criteria' has been created

Scenario: As a site administrator I can view a Blacklist Criteria
  Given a logged-in site administrator
    and a Blacklist Criteria 'My Blacklist Criteria'
   When I go to the Blacklist Criteria view
   Then I can see the Blacklist Criteria title 'My Blacklist Criteria'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Blacklist Criteria form
  Go To  ${PLONE_URL}/++add++Blacklist Criteria

a Blacklist Criteria 'My Blacklist Criteria'
  Create content  type=Blacklist Criteria  id=my-blacklist_criteria  title=My Blacklist Criteria


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form-widgets-IBasic-title  ${title}

I submit the form
  Click Button  Save

I go to the Blacklist Criteria view
  Go To  ${PLONE_URL}/my-blacklist_criteria
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Blacklist Criteria with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Blacklist Criteria title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
