import { api } from "config/axiosConfig"

export const petitionerService = {
    getPetitionerList: async () => {
        const response = await api.request({
            url: `/petitioner`,
            method: "GET",
        })
        return response.data
    },
    getPetitionerOverview: async (id) => {
        const response = await api.request({
            url: `/petitioner/overview/${id}`,
            method: "GET",
        })
        return response.data
    },
    getPetitionerIncorporation: async (id) => {
        const response = await api.request({
            url: `/petitioner/incorporation/${id}`,
            method: "GET",
        })
        return response.data
    },
    getPetitionerEmployeeRevenue: async (id) => {
        const response = await api.request({
            url: `/petitioner/employee_revenue/${id}`,
            method: "GET",
        })
        return response.data
    },
    getPetitionerImmigration: async (id) => {
        const response = await api.request({
            url: `/petitioner/immigration/${id}`,
            method: "GET",
        })
        return response.data
    },
    getPetitionerCompanyAuth: async (id) => {
        const response = await api.request({
            url: `/petitioner/company_auth/${id}`,
            method: "GET",
        })
        return response.data
    },
    getPetitionerContact: async (id) => {
        const response = await api.request({
            url: `/petitioner/contact/${id}`,
            method: "GET",
        })
        return response.data
    },
}
