import requests
cookies='store-idc=maliva;%20tt-target-idc=useast1a;%20passport_csrf_token=8d61780311359a828c44d3fc71926d31;%20passport_csrf_token_default=8d61780311359a828c44d3fc71926d31;%20store-country-code=dz;%20store-country-code-src=uid;%20d_ticket=fa47ea5a5a736ed7832c796a869c0bf616085;%20multi_sids=6907270777931711494%3A7579d1112e1d3e3fc3dbd3d9663db299%7C7394234693875057670%3A0fcd357489c911526b9df0e9eac8c8d3;%20odin_tt=a614b5395640c6f65241bb6c30523c7dbeed1d0e6b8f37d6e3e73f11a9e796259dd3918bf452793a7889401c11110268b64b756308076723c820e456c35ca71151bca4ed756246e83c3507ee032fb947;%20cmpl_token=AgQQAPMvF-RPsI_lYIqWPJ0__O-Q0kgJP4ekYNWr0A;%20sid_guard=7579d1112e1d3e3fc3dbd3d9663db299%7C1723071654%7C15552000%7CMon%2C+03-Feb-2025+23%3A00%3A54+GMT;%20uid_tt=17221740f000b2678a4a6a64bc7e8320e36434a14225e2b1ec9cce58a65d68a4;%20uid_tt_ss=17221740f000b2678a4a6a64bc7e8320e36434a14225e2b1ec9cce58a65d68a4;%20sid_tt=7579d1112e1d3e3fc3dbd3d9663db299;%20sessionid=7579d1112e1d3e3fc3dbd3d9663db299;%20sessionid_ss=7579d1112e1d3e3fc3dbd3d9663db299;%20install_id=7389856192924976902;%20ttreq=1$0d2e569624f35c738d2c54bb1ac8f202c82746ab;%20msToken=Tht9DGSb5xZ4eSnSwE_0DzueU47kDpxO46ebb06ElrNziYCwqpkMTk9fiFJC8_P-Fo-WFs73PYRx1Hf8Z2Kh9L5Veco8vcC4c31e7FUXhj2omPIjp8exxJ_CH6bV' #Example Cookies
install_id=7389856192924976902 #Install ID
device_id=7389854904419223045 #Device ID
secuid='MS4wLjABAAAAr5U_HUg-SS9ieJv-ZayCTZIzRsVNjM9xnUfJg7JPNk_fW-R0xuL7OhobYy267-v-' #User SecUID
uid=7065740413541712902 #User ID
response=requests.get(f'http://104.248.228.75:8080/follow?install_id={install_id}&device_id={device_id}&uid={uid}&secuid={secuid}&cook={cookies}').text
print(response)
