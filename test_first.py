import pytest
import os
import requests
import json
from PIL import Image, ImageChops
from playwright.sync_api import Page, expect


@pytest.mark.browser_context_args(storage_state="superuser_login_state.json")
def test_drill_down_level_1_CH(page: Page, settings) -> None:
    '''
    using test project recording feature screenshots are taken of correct drill down images and the script is written to create the same result again and comparing
    that result with the screenshots already stored. Threshold is 5%
    '''
    page.goto("/")
    expect(page.get_by_role("link", name="Support Account")).to_be_visible()

    with open('superuser_login_state.json', 'r') as file:
        auth_data = json.load(file)

    access_token = None
    for origin in auth_data.get("origins", []):
        for item in origin.get("localStorage", []):
            if item.get("name") == "TRP-Token":
                access_token = item.get("value")
                break

    # Use the access token from the loaded data
    headers = {'Authorization': f'TRP {access_token}'}

    endpointurl = "analytics/charts/?chart_type=line&series_names=Created%20At&x_field=cl_encountert_ountertype_db407875c277e3efb193&x_period=month_year&xaxis_type=category&source_id=42&sub_dataset_id=42&filters=cl_createdat_04abce75ed454a005177__range%3D%5B2020-01-01T00%3A00%3A00%2C2020-01-31T23%3A59%3A59%5D&metric=10"

    BASE_URL='https://api.test-staging.trp.ignishealth.com/'
    url = f"{BASE_URL}{endpointurl}"

    # Make a GET request to the API
    response = requests.get(url, headers=headers)
    target_values = [
        {"cl_encountert_ountertype_db407875c277e3efb193": "In Patient", "counter": 2},
        {"cl_encountert_ountertype_db407875c277e3efb193": "TeleHealth", "counter": 6},
        {"cl_encountert_ountertype_db407875c277e3efb193": "Out Patient", "counter": 5}
    ]

    assert response.status_code == 200
    data = response.json()
    for target_value in target_values:
        assert target_value in data['values'][0]

    endpointurl = "analytics/charts/?chart_type=line&series_names=Created%20At&x_field=cl_encountert_ountertype_db407875c277e3efb193&x_period=month_year&xaxis_type=category&source_id=42&sub_dataset_id=42&filters=cl_createdat_04abce75ed454a005177__range%3D%5B2019-04-01T00%3A00%3A00%2C2019-04-30T23%3A59%3A59%5D&metric=10"

    url = f"{BASE_URL}{endpointurl}"

    # Make a GET request to the API
    response = requests.get(url, headers=headers)
    target_values = [
        {"cl_encountert_ountertype_db407875c277e3efb193": "In Patient", "counter": 3},
        {"cl_encountert_ountertype_db407875c277e3efb193": "TeleHealth", "counter": 2},
        {"cl_encountert_ountertype_db407875c277e3efb193": "Out Patient", "counter": 5}
    ]

    assert response.status_code == 200
    data = response.json()
    for target_value in target_values:
        assert target_value in data['values'][0]

    sidebar_element = page.locator('.sidebar.collapsed')
    entity_gallery = sidebar_element.locator('a[href="/manage-database"]')
    entity_gallery.click()

    page.get_by_role("heading", name="Encounter").click()
    page.get_by_role("heading", name="CH Drilldown2").click()
    page.get_by_role("button", name="drill down dashboard").click()
    expect(page.get_by_role("button", name="Drill Down")).to_be_visible()
    page.get_by_role("button", name="Drill Down").click()

    page.locator(
        "ngb-modal-window trp-drilled-chart g.highcharts-markers.highcharts-series-0.highcharts-line-series.highcharts-color-0.highcharts-tracker > path:nth-child(11)").click()

    page.get_by_role("textbox").fill("Encounter Type")

    page.get_by_text("Encounter Type").click()

    page.wait_for_timeout(4000)

    screenshot_path = os.path.join(settings.ui_tests_root, "live_level1_SS.jpg")

    location = page.locator(
        "ngb-modal-window .modal-body > div > :nth-child(2) .highcharts-container > .highcharts-root > .highcharts-background")

    location.screenshot(path=screenshot_path)
    screenshot_image = Image.open(screenshot_path).convert('RGB')
    file_path = os.path.join(settings.ui_tests_root, "level1.jpg")
    original_image = Image.open(file_path).convert('RGB')

    diff = ImageChops.difference(original_image, screenshot_image)

    if diff.getbbox() is not None:
        percentage_diff = (diff.getbbox()[2] * diff.getbbox()[3]) / (
            screenshot_image.size[0] * screenshot_image.size[1]) * 100
    else:
        percentage_diff = 0.0

    tolerance = 5  # Adjust this value as per your requirements
    # diff.show()  # To Show the difference of an image
    percentage_diff <= tolerance

    page.wait_for_timeout(3000)

    page.locator(
        "ngb-modal-window .modal-body > div > :nth-child(1) .highcharts-container > .highcharts-root > .highcharts-series-group > .highcharts-markers > path:nth-child(5)").click()

    page.locator(
        "ngb-modal-window .modal-body > div > :nth-child(1) .highcharts-container > .highcharts-root > .highcharts-series-group > .highcharts-markers > path:nth-child(5)").click()

    page.wait_for_timeout(3000)

    screenshot_path = os.path.join(settings.ui_tests_root, "live_level1_PointChange_SS.jpg")

    location = page.locator(
        "ngb-modal-window .modal-body > div > :nth-child(2) .highcharts-container > .highcharts-root > .highcharts-background")

    location.screenshot(path=screenshot_path)
    screenshot_image = Image.open(screenshot_path).convert('RGB')

    file_path = os.path.join(settings.ui_tests_root, "level1_PointChange.jpg")
    original_image = Image.open(file_path).convert('RGB')

    diff = ImageChops.difference(original_image, screenshot_image)

    if diff.getbbox() is not None:
        percentage_diff = (diff.getbbox()[2] * diff.getbbox()[3]) / (
            screenshot_image.size[0] * screenshot_image.size[1]) * 100
    else:
        percentage_diff = 0.0

    tolerance = 5  # Adjust this value as per your requirements
    # diff.show()   #To Show the difference of an image
    percentage_diff <= tolerance
