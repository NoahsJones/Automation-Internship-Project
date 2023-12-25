# Created by noahsj at 12/19/2023
Feature: Secondary Page
  This page shows listing of properties that can be filtered and viewed to continue in a business action.

  Scenario: User can filter the Secondary deals by “want to sell” option
    Given Open sign-in page
    When Log in with email: noahsj@cox.net and password: Letter2021
    And Click on Secondary tab
    Then Verify Secondary page opens
    When Click on Filters
    And Filter for Want to sell
    Then Verify all cards have: For sale tag

  Scenario: Mobile - User can filter the Secondary deals by “want to sell” option
    Given Mobile - Open sign-in page
    When Mobile - Log in with email: noahsj@cox.net and password: Letter2021
    And Mobile - Tap on Off-Plan tab
    And Mobile - Tap on Secondary tab
    Then Mobile - Verify Secondary page opens
    When Mobile - Tap on Filters
    And Mobile - Filter for Want to sell
    Then Mobile - Verify all cards have: For sale tag
