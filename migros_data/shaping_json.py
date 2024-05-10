
def shaping_json(data):
    shaped_data = {
        "products": [

        ]
    }

    for i in range(len(data["product_name"])):
        temp_dict = {

                "product_id": "",
                "product_name": "",
                "product_image": "",
                "business_registration_number": "",
                "net_amount": "",
                "ingredients": [],
                "alergen_warnings": [],
                "company": ""
            }

        temp_dict["product_id"] = i
        temp_dict["product_name"] = data["product_name"][i]
        temp_dict["product_image"] = data["product_image"][i]
        temp_dict["business_registration_number"] = data["İşletme Kayıt No"][i]
        temp_dict["net_amount"] = data["Net Miktar (g/ml)"][i]
        temp_dict["ingredients"] = data["İçindekiler"][i]
        temp_dict["alergen_warnings"] = data["Alerjen Uyarısı"][i]
        temp_dict["company"] = data["Gıda İşletmecisi / Üretici / İthalatçı / Dağıtıcı"][i]

        shaped_data["products"].append(temp_dict)

    return shaped_data


