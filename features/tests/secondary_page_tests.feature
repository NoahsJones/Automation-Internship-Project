# Created by noahsj at 12/19/2023
Feature: Secondary Page
  This page shows listing of properties that can be filtered and viewed to continue in a business action.

  Scenario: User can filter the Secondary deals by “want to sell” option
    Given Open sign-in page
    When Log in with email: ***** and password: *****
    And Click on Secondary tab
    Then Verify Secondary page opens
    When Click on Filters
    And Filter for Want to sell
    Then Verify all cards have: for sale tag