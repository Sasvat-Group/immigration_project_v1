import { api } from 'config/axiosConfig'

export const beneficiaryService = {
    getBeneficiaryList: async () => {
        const data = await new Promise((resolve) =>
            setTimeout(
                () =>
                    resolve({
                        beneficiary: [
                            {
                                BeneficiaryID: 1310,
                                BeneficiaryName: 'IMMCorp 1'
                            },
                            {
                                BeneficiaryID: 1,
                                BeneficiaryName: 'IMMCorp 2'
                            },
                            {
                                BeneficiaryID: 2,
                                BeneficiaryName: 'IMMCorp 7'
                            }
                        ]
                    }),
                2000
            )
        )

        return data
    },
    getImmigrationTimeline: async (id) => {
        const response = await api.request({
            url: `/beneficiary/immigration_timeline/${id}`,
            method: 'GET'
        })
        return response.data
    },
    getQuickAssessmentForm: async (id) => {
        const response = await api.request({
            url: `/beneficiary/quick_assessment_form/${id}`,
            method: 'GET'
        })
        return response.data
    },
    getImmigrationStatusKeyDates: async (id) => {
        const response = await api.request({
            url: `/beneficiary/immigration_status_key_dates/${id}`,
            method: 'GET'
        })
        return response.data
    },
    getWorkAuthorizationInfo: async (id) => {
        const response = await api.request({
            url: `/beneficiary/work_authorization_info/${id}`,
            method: 'GET'
        })
        return response.data
    },
    getPriorityInfo: async (id) => {
        const response = await api.request({
            url: `/beneficiary/priority_info/${id}`,
            method: 'GET'
        })
        return response.data
    },
    getPRProcessInfo: async (id) => {
        const response = await api.request({
            url: `/beneficiary/pr_process_info/${id}`,
            method: 'GET'
        })
        return response.data
    },
    getEmploymentInfo: async (id) => {
        const response = await api.request({
            url: `/beneficiary/employment_info/${id}`,
            method: 'GET'
        })
        return response.data
    },
    getPassportTravel: async (id) => {
        const response = await api.request({
            url: `/beneficiary/passport_travel/${id}`,
            method: 'GET'
        })
        return response.data
    },
    getPersonalInfo: async (id) => {
        const response = await api.request({
            url: `/beneficiary/personal_info/${id}`,
            method: 'GET'
        })
        return response.data
    }
}
