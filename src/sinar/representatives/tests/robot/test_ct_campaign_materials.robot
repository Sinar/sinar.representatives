# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.representatives -t test_campaign_materials.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.representatives.testing.SINAR_REPRESENTATIVES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_campaign_materials.robot
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

Scenario: As a site administrator I can add a Campaign Materials
  Given a logged-in site administrator
    and an add Campaign Materials form
   When I type 'My Campaign Materials' into the title field
    and I submit the form
   Then a Campaign Materials with the title 'My Campaign Materials' has been created

Scenario: As a site administrator I can view a Campaign Materials
  Given a logged-in site administrator
    and a Campaign Materials 'My Campaign Materials'
   When I go to the Campaign Materials view
   Then I can see the Campaign Materials title 'My Campaign Materials'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Campaign Materials form
  Go To  ${PLONE_URL}/++add++Campaign Materials

a Campaign Materials 'My Campaign Materials'
  Create content  type=Campaign Materials  id=my-campaign_materials  title=My Campaign Materials


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form-widgets-IBasic-title  ${title}

I submit the form
  Click Button  Save

I go to the Campaign Materials view
  Go To  ${PLONE_URL}/my-campaign_materials
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Campaign Materials with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Campaign Materials title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
