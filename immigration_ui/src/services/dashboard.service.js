import { api } from "config/axiosConfig";

export const dashboardService = {
    getAllData: async () => {
        const response = await api.request({
            url: `/dashboard`,
            method: "GET",
        });
        return response.data;
    },
};
