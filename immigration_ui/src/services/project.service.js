import { api } from 'config/axiosConfig'

export const projectService = {
    rpaProcessActivate: () => {
        return api.request({
            url: '/rpa_quick_form_automation',
            method: 'GET'
        })
    }
}
