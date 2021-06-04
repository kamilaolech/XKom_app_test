class Locators():

    # Home Page PO:
    icons_class_name = 'android.widget.ImageView'          # list of elements: [-1] Profile, [-2] Basket, [-5] Home
    searchWindow_xpath = '//*[@text="Czego szukasz?"]'     # okno wyszukiwania
    searchedProduct_id = 'pl.xkom:id/phrase'               # produkt lub lista produktow wyszukanych

    # Profile Page PO:
    textInputWindows_class_name = 'android.widget.EditText' # list of elements: [0] email, [1] password
    loginButton_id = 'pl.xkom:id/loginButton'
    logoutButton_id = 'pl.xkom:id/action_logout'
    logoutConfirm1_id = 'pl.xkom:id/md_button_positive'
    logoutConfirm2_id = 'pl.xkom:id/md_button_positive'
    errorNotices_class_name = 'android.widget.TextView'     # list of elements

    # Product PO:
    price_id = 'pl.xkom:id/price'                           # cena produktu
    product_id = 'pl.xkom:id/name'                          # wyszukany produkt
    addToCart_accessibilityid = 'Do koszyka'                # dodaj do koszyka   #addToCart_xpath = '//*[@content-desc="Do koszyka"]'

    # Cart PO:
    totalProductsCost_id = 'pl.xkom:id/basketTotalCostValue'

