import React from "react";
import Body from "../PageComponents/Body"

const LayoutOne = ({ 
    body, 
    editable, 
    entry
}) => {

    body.current = entry.body;
    const classImage = "single-image"

    return (
        <Body 
        editable={editable}
        body={body}
     />
    )
}

export default LayoutOne;