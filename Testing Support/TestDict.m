#import @"XYZGeometry.h"

@implementation ProblemChild	

- (void)testDict {
    NSDictionary *dictReqPrm = @{@"reqparam": @{@"session": NSAssureNotNill(sSess), @"ac": @"snsPost"},
                                                   @"content": NSAssureNotNill(self.tvContent.text),
                                                   @"siteurl": NSAssureNotNill(sHyperlink),
                                                   @"sitetitle": NSAssureNotNill(strLinkTitle),
                                                   @"siteimg": NSAssureNotNill(strLinkImageUrl)};

    NSDictionary *param = @{@"thumb": thumb,
                          @"tagids": @"",
                          @"airtime": @(0),
                          @"title": title,
                          @"gameid": @(gameId),
                          @"sdk_type": @(sdkType),
                          @"a": [a b]};

    NSError *error = [NSError errorWithDomain:NSCocoaErrorDomain code:0 userInfo:@{NSLocalizedDescriptionKey: @"stop",
                                                                                 NSLocalizedFailureReasonErrorKey: errString}];

    NSError *error = [NSError errorWithDomain:NSCocoaErrorDomain code:0 userInfo:@{NSLocalizedDescriptionKey: @"stop",
                                                                                 NSLocalizedFailureReasonErrorKey: LANG(@"common_net_connect_error")}];
}

@end
