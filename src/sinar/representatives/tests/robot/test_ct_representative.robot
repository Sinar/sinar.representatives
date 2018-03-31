# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s sinar.representatives -t test_representative.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src sinar.representatives.testing.SINAR_REPRESENTATIVES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_representative.robot
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

Scenario: As a site administrator I can add a representative
  Given a logged-in site administrator
    and an add representative form
   When I type 'My Representative' into the title field
    and I submit the form
   Then a representative with the title 'My Representative' has been created

Scenario: As a site administrator I can view a representative
  Given a logged-in site administrator
    and a representative 'My Representative'
   When I go to the representative view
   Then I can see the representative title 'My Representative'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add representative form
  Go To  ${PLONE_URL}/++add++representative

a representative 'My Representative'
  Create content  type=representative  id=my-representative  title=My Representative


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IDublinCore.title  ${title}

I submit the form
  Click Button  Save

I go to the representative view
  Go To  ${PLONE_URL}/my-representative
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a representative with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the representative title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
