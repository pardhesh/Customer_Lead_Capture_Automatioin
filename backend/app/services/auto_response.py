def get_auto_response(category: str) -> str:
    
    if category == "Hot Lead":
        return (
            "Thank you for reaching out and strong interest. "
            "Our sales team will immediatley contact you shortly with details."
        )

    if category == "Medium Lead":
        return (
            "Thanks for your interest."
            "We will share details and catalog information shortly."
        )

    if category == "Low Lead":
        return (
            "Thank you for contacting us. "
            "You can explore our products on our website for more information."
        )

    if category == "Support":
        return (
            "Thanks for reaching out. "
            "Your request has been forwarded to our support team."
        )
    #if none of the above. very rare to be this
    return "Thank you for contacting us."
