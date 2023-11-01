export function textValidator(value, defaultValue = 'NA') {

    if (value && typeof value === 'boolean')
        return value ? 'Yes' : 'No'

    return value || defaultValue
}

export function trimDate(value) {
    return value?.toString().replaceAll(' 00:00:00 GMT', '')
}