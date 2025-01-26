Feature:
  Scenario: Launch Facebook url
    Given launch chrome driver
    When open facebook home page
    Then verify the logo presence
    And close browser
    git config --global user.email "somasamarth@gmail.com"
