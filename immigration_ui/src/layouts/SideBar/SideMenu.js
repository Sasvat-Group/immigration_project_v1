export const MENUITEMS = [
	{
		menutitle: 'DASHBOARD',
		Items: [
			{
				path: `${process.env.PUBLIC_URL}/dashboard`,
				icon: 'ti-home',
				type: 'link',
				active: false,
				selected: false,
				title: 'My Dashboard'
			},
			{
				title: 'Patitioner Info',
				path: `${process.env.PUBLIC_URL}/petitioner-info`,
				icon: 'ti-bar-chart-alt',
				type: 'link',
				active: false,
				selected: false,
				children: []
			},
			{
				title: 'Beneficiary Info',
				path: `${process.env.PUBLIC_URL}/beneficiary`,
				icon: 'ti-user',
				type: 'link',
				active: false,
				selected: false,
				children: []
			},
			{
				title: 'Project Info',
				path: `${process.env.PUBLIC_URL}/case-info`,
				icon: 'ti-file',
				type: 'sub',
				children: [
					{
						path: `${process.env.PUBLIC_URL}/case-info/overview`,
						type: 'link',
						active: false,
						selected: false,
						title: 'Project Overview'
					},
					{
						path: `${process.env.PUBLIC_URL}/case-info/process`,
						type: 'link',
						active: false,
						selected: false,
						title: 'Project Process'
					},
					{
						path: `${process.env.PUBLIC_URL}/case-info/specific`,
						type: 'link',
						active: false,
						selected: false,
						title: 'Project Specific Data'
					}
				]
			},
			{
				title: 'PERM Info',
				path: `${process.env.PUBLIC_URL}/PERM-info`,
				icon: 'ti-bar-chart',
				type: 'sub',
				children: [
					{
						path: `${process.env.PUBLIC_URL}/PERM-info/cases`,
						type: 'link',
						active: false,
						selected: false,
						title: 'PERM Projects'
					},
					{
						path: `${process.env.PUBLIC_URL}/PERM-info/overall`,
						type: 'link',
						active: false,
						selected: false,
						title: 'PERM Overall'
					}
				]
			},
			{
				title: 'Documents',
				icon: 'ti-folder',
				path: `${process.env.PUBLIC_URL}/documents`,
				type: 'link',
				active: false,
				selected: false,
				children: []
			},
			{
				title: 'Integrations',
				icon: 'ti-settings',
				path: `${process.env.PUBLIC_URL}/integrations`,
				type: 'link',
				active: false,
				selected: false,
				children: []
			},
			{
				title: 'Compliance Info',
				icon: 'ti-folder',
				path: `${process.env.PUBLIC_URL}/compliance-info`,
				type: 'link',
				active: false,
				selected: false,
				children: []
			},
			{
				title: 'Reports',
				icon: 'ti-panel',
				path: `${process.env.PUBLIC_URL}/reports`,
				type: 'link',
				active: false,
				selected: false,
				children: []
			},
			{
				title: 'Quick Links',
				path: `${process.env.PUBLIC_URL}/quick-links`,
				icon: 'ti-link',
				type: 'link',
				active: false,
				selected: false,
				children: []
			},
			{
				title: 'Immigration Toolkit',
				icon: 'ti-harddrives',
				path: `${process.env.PUBLIC_URL}/toolkit`,
				type: 'link',
				active: false,
				selected: false,
				children: []
			},
			{
				title: 'Admin View',
				path: `${process.env.PUBLIC_URL}/admin-view`,
				icon: 'ti-user',
				type: 'sub',
				active: false,
				selected: false,
				children: []
			},
			{
				title: 'Marketplace',
				icon: 'ti-shopping-cart-full',
				path: `${process.env.PUBLIC_URL}/marketplace`,
				type: 'link',
				active: false,
				selected: false,
				children: []
			}
		]
	}
]


export const BENEFICIARY_MENUITEMS = [
	{
		menutitle: 'DASHBOARD',
		Items: [
			{
				title: 'Beneficiary Info',
				path: `${process.env.PUBLIC_URL}/beneficiary`,
				icon: 'ti-user',
				type: 'link',
				active: false,
				selected: false,
				children: []
			},
			{
				title: 'Project Info',
				path: `${process.env.PUBLIC_URL}/case-info`,
				icon: 'ti-file',
				type: 'sub',
				children: [
					{
						path: `${process.env.PUBLIC_URL}/case-info/specific`,
						type: 'link',
						active: false,
						selected: false,
						title: 'Project Specific Data'
					}
				]
			},
		]
	}
]
