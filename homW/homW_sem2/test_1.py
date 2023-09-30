import random
import string
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def get_random_text(len_text):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len_text))


def test_step1(site):
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == "401"


def test_step2(site, selector_input_login, selector_input_password, selector_button, selector_error):
    input1 = site.find_element("xpath", selector_input_login)
    input1.send_keys("test")
    input2 = site.find_element("xpath", selector_input_password)
    input2.send_keys("test")
    btn = site.find_element("css", selector_button)
    btn.click()
    err_label = site.find_element("xpath", selector_error)
    assert err_label.text == "401"


def test_step3(site, selector_input_login, selector_input_password, selector_button, selector_blog):
    input1 = site.find_element("xpath", selector_input_login)
    input1.clear()
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", selector_input_password)
    input2.clear()
    input2.send_keys(testdata['password'])
    btn = site.find_element("css", selector_button)
    btn.click()
    blog = site.find_element("xpath", selector_blog)
    assert blog.text == "Blog"


def test_step4_hw(site, selector_input_login, selector_input_password, selector_button, selector_create,
                  selector_title_create,
                  selector_description_create, selector_content_create, selector_title_public,
                  selector_content_public):
    input1 = site.find_element_wait_located("xpath", selector_input_login)
    input1.clear()
    input1.send_keys(testdata['login'])

    input2 = site.find_element_wait_located("xpath", selector_input_password)
    input2.clear()
    input2.send_keys(testdata['password'])

    btn = site.find_element_wait_clickable("xpath", selector_button)
    btn.click()

    btn_create = site.find_element_wait_clickable("xpath", selector_create)
    btn_create.click()

    title_text = get_random_text(10)
    description_text = get_random_text(20)
    content_text = get_random_text(50)

    title = site.find_element_wait_located("xpath", selector_title_create)
    title.send_keys(title_text)

    description = site.find_element_wait_located("xpath", selector_description_create)
    description.send_keys(description_text)

    content = site.find_element_wait_located("xpath", selector_content_create)
    content.send_keys(content_text)

    save = site.find_element_wait_clickable("xpath", selector_button)
    save.click()

    element_title_text = site.find_element_wait_located("xpath", selector_title_public).text
    element_content_text = site.find_element_wait_located("xpath", selector_content_public).text
    assert element_title_text == title_text
    assert element_content_text == content_text