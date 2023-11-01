import { api } from "config/axiosConfig";

export const loginService = {
    signIn: ({ username, password }) => {
        return api.request({
            url: "/signin",
            method: "GET",
            auth: {
                username,
                password,
            },
        });
    },
};
