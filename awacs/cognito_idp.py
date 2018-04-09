# Copyright (c) 2012-2013, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.

from aws import Action as BaseAction
from aws import BaseARN

service_name = 'Amazon Cognito User Pools'
prefix = 'cognito-idp'


class Action(BaseAction):
    def __init__(self, action=None):
        sup = super(Action, self)
        sup.__init__(prefix, action)


class ARN(BaseARN):
    def __init__(self, resource='', region='', account=''):
        sup = super(ARN, self)
        sup.__init__(service=prefix, resource=resource, region=region,
                     account=account)


AddCustomAttributes = Action('AddCustomAttributes')
AdminAddUserToGroup = Action('AdminAddUserToGroup')
AdminConfirmSignUp = Action('AdminConfirmSignUp')
AdminCreateUser = Action('AdminCreateUser')
AdminDeleteUser = Action('AdminDeleteUser')
AdminDeleteUserAttributes = Action('AdminDeleteUserAttributes')
AdminDisableUser = Action('AdminDisableUser')
AdminEnableUser = Action('AdminEnableUser')
AdminForgetDevice = Action('AdminForgetDevice')
AdminGetDevice = Action('AdminGetDevice')
AdminGetUser = Action('AdminGetUser')
AdminInitiateAuth = Action('AdminInitiateAuth')
AdminListDevices = Action('AdminListDevices')
AdminListGroupsForUser = Action('AdminListGroupsForUser')
AdminListUserAuthEvents = Action('AdminListUserAuthEvents')
AdminRemoveUserFromGroup = Action('AdminRemoveUserFromGroup')
AdminResetUserPassword = Action('AdminResetUserPassword')
AdminRespondToAuthChallenge = Action('AdminRespondToAuthChallenge')
AdminSetUserMFAPreference = Action('AdminSetUserMFAPreference')
AdminSetUserSettings = Action('AdminSetUserSettings')
AdminUpdateAuthEventFeedback = Action('AdminUpdateAuthEventFeedback')
AdminUpdateDeviceStatus = Action('AdminUpdateDeviceStatus')
AdminUpdateUserAttributes = Action('AdminUpdateUserAttributes')
AdminUserGlobalSignOut = Action('AdminUserGlobalSignOut')
ChangePassword = Action('ChangePassword')
ConfirmDevice = Action('ConfirmDevice')
ConfirmForgotPassword = Action('ConfirmForgotPassword')
ConfirmSignUp = Action('ConfirmSignUp')
CreateGroup = Action('CreateGroup')
CreateUserImportJob = Action('CreateUserImportJob')
CreateUserPool = Action('CreateUserPool')
CreateUserPoolClient = Action('CreateUserPoolClient')
DeleteGroup = Action('DeleteGroup')
DeleteUser = Action('DeleteUser')
DeleteUserAttributes = Action('DeleteUserAttributes')
DeleteUserPool = Action('DeleteUserPool')
DeleteUserPoolClient = Action('DeleteUserPoolClient')
DescribeRiskConfiguration = Action('DescribeRiskConfiguration')
DescribeUserImportJob = Action('DescribeUserImportJob')
DescribeUserPool = Action('DescribeUserPool')
DescribeUserPoolClient = Action('DescribeUserPoolClient')
ForgetDevice = Action('ForgetDevice')
ForgotPassword = Action('ForgotPassword')
GetCSVHeader = Action('GetCSVHeader')
GetDevice = Action('GetDevice')
GetGroup = Action('GetGroup')
GetUser = Action('GetUser')
GetUserAttributeVerificationCode = \
    Action('GetUserAttributeVerificationCode')
GetUserPoolMfaConfig = Action('GetUserPoolMfaConfig')
GlobalSignOut = Action('GlobalSignOut')
InitiateAuth = Action('InitiateAuth')
ListDevices = Action('ListDevices')
ListGroups = Action('ListGroups')
ListUserImportJobs = Action('ListUserImportJobs')
ListUserPoolClients = Action('ListUserPoolClients')
ListUsersInGroup = Action('ListUsersInGroup')
ResendConfirmationCode = Action('ResendConfirmationCode')
RespondToAuthChallenge = Action('RespondToAuthChallenge')
SetRiskConfiguration = Action('SetRiskConfiguration')
SetUserMFAPreference = Action('SetUserMFAPreference')
SetUserPoolMfaConfig = Action('SetUserPoolMfaConfig')
SetUserSettings = Action('SetUserSettings')
SignUp = Action('SignUp')
StartUserImportJob = Action('StartUserImportJob')
StopUserImportJob = Action('StopUserImportJob')
UpdateAuthEventFeedback = Action('UpdateAuthEventFeedback')
UpdateDeviceStatus = Action('UpdateDeviceStatus')
UpdateGroup = Action('UpdateGroup')
UpdateUserAttributes = Action('UpdateUserAttributes')
UpdateUserPool = Action('UpdateUserPool')
UpdateUserPoolClient = Action('UpdateUserPoolClient')
VerifyUserAttribute = Action('VerifyUserAttribute')
