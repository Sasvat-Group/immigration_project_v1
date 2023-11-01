import React from "react";
import { useLocation } from "react-router-dom";

export default function useFetch() {
    const appUser = useLocation().state;

    console.log("appUser", appUser);

    return <div>useFetch</div>;
}
